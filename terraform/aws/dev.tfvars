aws_region   = "us-east-1"
aws_profile  = "default"

project      = "lakehouse"
environment  = "dev"

vpc_id       = "vpc-xxxxxxxx"
subnet_ids   = ["subnet-aaaa1111", "subnet-bbbb2222"]
ec2_keypair  = "dev-keypair"

# MSK
kafka_version       = "2.8.1"
kafka_brokers       = 2
kafka_instance_type = "kafka.t3.small"

# Redshift
redshift_node_type     = "dc2.large"
redshift_nodes         = 1
redshift_master_user   = "adminuser"
redshift_master_password = "DevSecret123!"

# DMS
dms_instance_class = "dms.t3.micro"
dms_storage        = 20

# Lambda
lambda_runtime   = "python3.9"
lambda_handler   = "lambda_function.lambda_handler"
lambda_filename  = "lambda_dev.zip"

# Pipeline
pipeline_source_bucket = "lakehouse-dev-source"
pipeline_source_object = "source.zip"

default_tags = {
  Environment = "dev"
  Owner       = "DataTeam"
  CostCenter  = "DEV-001"
}
