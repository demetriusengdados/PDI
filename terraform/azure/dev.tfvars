terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# Variáveis principais
variable "azure_region" { default = "eastus" }
variable "project"      { default = "lakehouse" }
variable "environment"  { default = "dev" }

locals {
  rg_name = "${var.project}-${var.environment}-rg"
  tags = {
    Environment = "dev"
    Owner       = "DataTeam"
    CostCenter  = "DEV-001"
  }
}

# Resource Group
resource "azurerm_resource_group" "main" {
  name     = local.rg_name
  location = var.azure_region
  tags     = local.tags
}

# Networking
resource "azurerm_virtual_network" "vnet" {
  name                = "vnet-${var.project}-${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  address_space       = ["10.0.0.0/16"]
  tags                = local.tags
}

resource "azurerm_subnet" "subnet_a" {
  name                 = "subnet-a"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}

resource "azurerm_subnet" "subnet_b" {
  name                 = "subnet-b"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.2.0/24"]
}

# Storage Account
resource "azurerm_storage_account" "storage" {
  name                     = "lakehousedevstore"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  tags                     = local.tags
}

resource "azurerm_storage_container" "source" {
  name                  = "source"
  storage_account_id    = azurerm_storage_account.storage.id
  container_access_type = "private"
}

# Event Hubs (Kafka API)
resource "azurerm_eventhub_namespace" "eh_ns" {
  name                = "lakehouse-dev-eh"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  sku                 = "Standard"
  capacity            = 1
  tags                = local.tags
}

resource "azurerm_eventhub" "eh" {
  name                   = "lakehouse-kafka"
  eventhub_namespace_id  = azurerm_eventhub_namespace.eh_ns.id
  resource_group_name    = azurerm_resource_group.main.name
  partition_count        = 2
  message_retention      = 1
}

# Synapse Analytics
resource "azurerm_synapse_workspace" "synapse_ws" {
  name                                 = "lakehouse-dev-synapse"
  resource_group_name                  = azurerm_resource_group.main.name
  location                             = azurerm_resource_group.main.location
  storage_data_lake_gen2_filesystem_id = azurerm_storage_container.source.id
  sql_administrator_login              = "adminuser"
  sql_administrator_login_password     = "DevSecret123!"
  tags                                 = local.tags
}

resource "azurerm_synapse_sql_pool" "sqlpool" {
  name                   = "devsqlpool"
  synapse_workspace_id   = azurerm_synapse_workspace.synapse_ws.id
  sku_name               = "DW100c"
  create_mode            = "Default"
  storage_account_type   = "GRS"
}

# Database Migration Service
resource "azurerm_database_migration_service" "dms" {
  name                = "lakehouse-dms-dev"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  sku_name            = "Basic_1vCore"
  subnet_id           = azurerm_subnet.subnet_a.id
  tags                = local.tags
}

# Azure Function App (Python 3.9)
resource "azurerm_app_service_plan" "func_plan" {
  name                = "func-plan-${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  kind                = "FunctionApp"
  reserved            = true
  sku {
    tier = "Dynamic"
    size = "Y1"
  }
}

resource "azurerm_function_app" "function" {
  name                       = "lakehouse-dev-func"
  location                   = azurerm_resource_group.main.location
  resource_group_name        = azurerm_resource_group.main.name
  app_service_plan_id        = azurerm_app_service_plan.func_plan.id
  storage_account_name       = azurerm_storage_account.storage.name
  storage_account_access_key = azurerm_storage_account.storage.primary_access_key
  version                    = "~3"
  os_type                    = "linux"

  app_settings = {
    FUNCTIONS_WORKER_RUNTIME = "python"
    WEBSITE_RUN_FROM_PACKAGE = "https://${azurerm_storage_account.storage.name}.blob.core.windows.net/${azurerm_storage_container.source.name}/source.zip"
  }

  tags = local.tags
}
