terraform {
  required_version = ">= 1.3.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile
}

# -----------------------
# S3 Data Lake
# -----------------------
module "s3_lakehouse" {
  source  = "terraform-aws-modules/s3-bucket/aws"
  version = "~> 4.0"

  bucket        = "${var.project}-lakehouse-${var.environment}"
  force_destroy = true

  versioning = {
    enabled = true
  }

  tags = {
    Environment = var.environment
    Project     = var.project
  }
}

# -----------------------
# KMS Key (para S3, Glue, Redshift etc.)
# -----------------------
resource "aws_kms_key" "lakehouse_kms" {
  description             = "KMS key for ${var.project}-${var.environment}"
  deletion_window_in_days = 10
  enable_key_rotation     = true

  tags = {
    Environment = var.environment
    Project     = var.project
  }
}

# -----------------------
# IAM Roles & Policies
# -----------------------
resource "aws_iam_role" "lakehouse_role" {
  name               = "${var.project}-role-${var.environment}"
  assume_role_policy = data.aws_iam_policy_document.lakehouse_assume.json
}

data "aws_iam_policy_document" "lakehouse_assume" {
  statement {
    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["glue.amazonaws.com", "lambda.amazonaws.com", "ec2.amazonaws.com", "redshift.amazonaws.com", "dms.amazonaws.com"]
    }
    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role_policy_attachment" "lakehouse_admin_attach" {
  role       = aws_iam_role.lakehouse_role.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

# -----------------------
# MSK Kafka Cluster
# -----------------------
resource "aws_msk_cluster" "kafka" {
  cluster_name           = "${var.project}-kafka-${var.environment}"
  kafka_version          = var.kafka_version
  number_of_broker_nodes = var.kafka_brokers

  broker_node_group_info {
    instance_type   = var.kafka_instance_type
    client_subnets  = var.subnet_ids
    security_groups = [aws_security_group.kafka_sg.id]
  }

  encryption_info {
    encryption_at_rest_kms_key_arn = aws_kms_key.lakehouse_kms.arn
  }

  tags = {
    Environment = var.environment
    Project     = var.project
  }
}

resource "aws_security_group" "kafka_sg" {
  name        = "${var.project}-kafka-sg-${var.environment}"
  vpc_id      = var.vpc_id
  description = "Security group for Kafka brokers"

  ingress {
    from_port   = 9092
    to_port     = 9092
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # ajustar
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# -----------------------
# AWS Glue Data Catalog
# -----------------------
resource "aws_glue_catalog_database" "lakehouse_db" {
  name = "${var.project}_db_${var.environment}"
}

resource "aws_glue_catalog_table" "lakehouse_table" {
  name          = "example_table"
  database_name = aws_glue_catalog_database.lakehouse_db.name
  table_type    = "EXTERNAL_TABLE"
}

# -----------------------
# Athena Workgroup
# -----------------------
resource "aws_athena_workgroup" "lakehouse_wg" {
  name = "${var.project}_wg_${var.environment}"

  configuration {
    result_configuration {
      output_location = "s3://${module.s3_lakehouse.s3_bucket_id}/athena-results/"
    }
  }
}

# -----------------------
# Redshift Cluster
# -----------------------
resource "aws_redshift_cluster" "lakehouse_redshift" {
  cluster_identifier      = "${var.project}-redshift-${var.environment}"
  node_type               = "dc2.large"
  number_of_nodes         = 2
  master_username         = "adminuser"
  master_password         = "SuperSecret123!"
  iam_roles               = [aws_iam_role.lakehouse_role.arn]
  encrypted               = true
  kms_key_id              = aws_kms_key.lakehouse_kms.arn
  skip_final_snapshot     = true
  publicly_accessible     = false
}

# -----------------------
# DMS (Database Migration Service)
# -----------------------
resource "aws_dms_replication_instance" "lakehouse_dms" {
  replication_instance_id     = "${var.project}-dms-${var.environment}"
  replication_instance_class  = "dms.t3.medium"
  allocated_storage           = 50
  publicly_accessible         = false
}

# -----------------------
# Lambda (exemplo para ETL)
# -----------------------
resource "aws_lambda_function" "lakehouse_lambda" {
  function_name = "${var.project}-lambda-${var.environment}"
  role          = aws_iam_role.lakehouse_role.arn
  runtime       = "python3.9"
  handler       = "lambda_function.lambda_handler"

  filename      = "lambda.zip"
}

# -----------------------
# Lake Formation (habilita no Data Lake)
# -----------------------
resource "aws_lakeformation_data_lake_settings" "settings" {
  admins = [aws_iam_role.lakehouse_role.arn]
}

# -----------------------
# EC2 para Producers/Consumers
# -----------------------
resource "aws_instance" "lakehouse_ec2" {
  ami                    = "ami-0c55b159cbfafe1f0" # ajustar para sua região
  instance_type          = "t3.micro"
  subnet_id              = element(var.subnet_ids, 0)
  vpc_security_group_ids = [aws_security_group.kafka_sg.id]
  key_name               = var.ec2_keypair

  tags = {
    Name        = "${var.project}-ec2-${var.environment}"
    Environment = var.environment
  }
}

# -----------------------
# CodePipeline + CodeBuild + CodeDeploy (CI/CD exemplo)
# -----------------------
resource "aws_codepipeline" "lakehouse_pipeline" {
  name     = "${var.project}-pipeline-${var.environment}"
  role_arn = aws_iam_role.lakehouse_role.arn

  artifact_store {
    type     = "S3"
    location = module.s3_lakehouse.s3_bucket_id
  }

  stage {
    name = "Source"
    action {
      name             = "SourceAction"
      category         = "Source"
      owner            = "AWS"
      provider         = "S3"
      version          = "1"
      output_artifacts = ["source_output"]

      configuration = {
        S3Bucket = module.s3_lakehouse.s3_bucket_id
        S3ObjectKey = "source.zip"
      }
    }
  }

  stage {
    name = "Build"
    action {
      name             = "BuildAction"
      category         = "Build"
      owner            = "AWS"
      provider         = "CodeBuild"
      version          = "1"
      input_artifacts  = ["source_output"]
      output_artifacts = ["build_output"]

      configuration = {
        ProjectName = aws_codebuild_project.lakehouse_build.name
      }
    }
  }
}

resource "aws_codebuild_project" "lakehouse_build" {
  name          = "${var.project}-build-${var.environment}"
  service_role  = aws_iam_role.lakehouse_role.arn

  artifacts {
    type = "CODEPIPELINE"
  }

  environment {
    compute_type                = "BUILD_GENERAL1_SMALL"
    image                       = "aws/codebuild/standard:5.0"
    type                        = "LINUX_CONTAINER"
    privileged_mode             = true
  }

  source {
    type = "CODEPIPELINE"
  }
}

resource "aws_codedeploy_app" "lakehouse_app" {
  name = "${var.project}-codedeploy-${var.environment}"
  compute_platform = "Server"
}

resource "aws_codedeploy_deployment_group" "lakehouse_dg" {
  app_name              = aws_codedeploy_app.lakehouse_app.name
  deployment_group_name = "${var.project}-dg-${var.environment}"
  service_role_arn      = aws_iam_role.lakehouse_role.arn
  ec2_tag_set {
    ec2_tag_filter {
      key   = "Environment"
      type  = "KEY_AND_VALUE"
      value = var.environment
    }
  }
}
