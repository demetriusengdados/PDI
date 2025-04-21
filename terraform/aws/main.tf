provider "aws" {
  region = "us-east-1"
}

module "s3_lakehouse" {
  source = "terraform-aws-modules/s3-bucket/aws"
  bucket = "lakehouse-dados"
  versioning = true
}

resource "aws_msk_cluster" "kafka" {
  cluster_name           = "kafka-lakehouse"
  kafka_version          = "2.8.1"
  number_of_broker_nodes = 3
  // outros parâmetros...
}
