aws_region   = "us-east-1"
aws_profile  = "prod"

project      = "lakehouse"
environment  = "prod"

vpc_id       = "vpc-zzzzzzzz"
subnet_ids   = ["subnet-eeee5555", "subnet-ffff6666", "subnet-gggg7777"]
ec2_keypair  = "prod-keypair"

# MSK
kafka_version       = "3.4.0"
kafka_brokers       = 6
kafka_instance_type = "kafka.m5.xlarge"

# Redshift
redshift_node_type     = "ra3.xlplus"
redshift_nodes         = 3
redshift_master_user   = "adminuser"
redshift_master_password = "ProdSuperSecret123!"

# DMS
dms_instance_class = "dms.r5.large"
dms_storage        = 200

# Lambda
lambda_runtime   = "python3.9"
lambda_handler   = "lambda_function.lambda_handler"
lambda_filename  = "lambda_prod.zip"

# Pipeline
pipeline_source_bucket = "lakehouse-prod-source"
pipeline_source_object = "source.zip"

default_tags = {
  Environment = "prod"
  Owner       = "DataTeam"
  CostCenter  = "PROD-001"
  Criticality = "High"
}
