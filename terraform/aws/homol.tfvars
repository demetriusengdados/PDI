aws_region   = "us-east-1"
aws_profile  = "default"

project      = "lakehouse"
environment  = "homol"

vpc_id       = "vpc-yyyyyyyy"
subnet_ids   = ["subnet-cccc3333", "subnet-dddd4444"]
ec2_keypair  = "homol-keypair"

# MSK
kafka_version       = "2.8.1"
kafka_brokers       = 3
kafka_instance_type = "kafka.m5.large"

# Redshift
redshift_node_type     = "dc2.large"
redshift_nodes         = 2
redshift_master_user   = "adminuser"
redshift_master_password = "HomolSecret123!"

# DMS
dms_instance_class = "dms.t3.medium"
dms_storage        = 50

# Lambda
lambda_runtime   = "python3.9"
lambda_handler   = "lambda_function.lambda_handler"
lambda_filename  = "lambda_homol.zip"

# Pipeline
pipeline_source_bucket = "lakehouse-homol-source"
pipeline_source_object = "source.zip"

default_tags = {
  Environment = "homol"
  Owner       = "DataTeam"
  CostCenter  = "HOMOL-001"
}
