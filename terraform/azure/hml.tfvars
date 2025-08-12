# Azure General
azure_region  = "eastus"
azure_profile = "default"

project       = "lakehouse"
environment   = "hml"

# Networking
vnet_name     = "vnet-lakehouse-hml"
subnet_names  = ["subnet-c", "subnet-d"]
ssh_key_name  = "homol-keypair"

# Event Hubs (Kafka API)
eventhub_namespace       = "lakehouse-hml-eh"
eventhub_name            = "lakehouse-kafka"
eventhub_partition_count = 3
eventhub_throughput_units = 2  # mais brokers -> mais throughput

# Synapse Analytics
synapse_workspace_name = "lakehouse-hml-synapse"
synapse_sql_pool_name  = "hmlsqlpool"
synapse_sql_pool_size  = "DW200c"  # ajustado para ~dc2.large com 2 nós
synapse_admin_user     = "adminuser"
synapse_admin_password = "HomolSecret123!"

# Database Migration Service
dms_service_name = "lakehouse-dms-hml"
dms_sku          = "Standard_2vCores"  # mais próximo de dms.t3.medium
dms_storage_gb   = 50

# Azure Functions
function_runtime   = "python|3.9"
function_handler   = "lambda_function.lambda_handler"
function_package   = "lambda_homol.zip"

# Storage (Blob)
storage_account_name   = "lakehousehmlstore"
storage_container_name = "source"
storage_blob_name      = "source.zip"

# Tags
default_tags = {
  Environment = "hml"
  Owner       = "DataTeam"
  CostCenter  = "HML-001"
}
