provider "azurerm" {
  features {}
}

resource "azurerm_storage_account" "lakehouse" {
  name                     = "lakehousestorage"
  resource_group_name      = "data-platform"
  location                 = "East US"
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
