# Azure General
azure_region  = "eastus"
azure_profile = "default"

project       = "lakehouse"
environment   = "prod"

# Networking
vnet_name     = "vnet-lakehouse-prod"
subnet_names  = ["subnet-x", "subnet-y"]
ssh_key_name  = "prod-keypair"

# Event Hubs (Kafka API)
eventhub_namespace       = "lakehouse-prod-eh"
eventhub_name            = "lakehouse-kafka"
eventhub_partition_count = 6          # alta concorrência
eventhub_throughput_units = 4         # mais throughput que hml/dev

# Synapse Analytics
synapse_workspace_name = "lakehouse-prod-synapse"
synapse_sql_pool_name  = "prodsqlpool"
synapse_sql_pool_size  = "DW400c"      # capacidade maior para prod
synapse_admin_user     = "adminuser"
synapse_admin_password = "ProdSecret123!"

# Database Migration Service
dms_service_name = "lakehouse-dms-prod"
dms_sku          = "Premium_4vCores"   # mais processamento para cargas grandes
dms_storage_gb   = 200

# Azure Functions
function_runtime   = "python|3.9"
function_handler   = "lambda_function.lambda_handler"
function_package   = "lambda_prod.zip"

# Storage (Blob)
storage_account_name   = "lakehouseprodstorage"
storage_container_name = "source"
storage_blob_name      = "source.zip"

# Tags
default_tags = {
  Environment = "prod"
  Owner       = "DataTeam"
  CostCenter  = "PROD-001"
}
