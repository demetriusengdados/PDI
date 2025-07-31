# -----------------------
# Configurações básicas
# -----------------------
variable "aws_region" {
  description = "Região AWS onde os recursos serão criados"
  type        = string
  default     = "us-east-1"
}

variable "aws_profile" {
  description = "Perfil AWS CLI usado para autenticação"
  type        = string
  default     = "default"
}

variable "project" {
  description = "Nome do projeto"
  type        = string
  default     = "lakehouse"
}

variable "environment" {
  description = "Ambiente (dev, homol, prod)"
  type        = string
}

# -----------------------
# Rede
# -----------------------
variable "vpc_id" {
  description = "VPC onde os recursos serão criados"
  type        = string
}

variable "subnet_ids" {
  description = "Lista de subnets para os serviços (MSK, EC2, etc.)"
  type        = list(string)
}

variable "ec2_keypair" {
  description = "Nome do keypair para acesso SSH em instâncias EC2"
  type        = string
}

# -----------------------
# MSK (Kafka)
# -----------------------
variable "kafka_version" {
  description = "Versão do Kafka a ser usada no MSK"
  type        = string
  default     = "2.8.1"
}

variable "kafka_brokers" {
  description = "Número de brokers no cluster MSK"
  type        = number
  default     = 3
}

variable "kafka_instance_type" {
  description = "Tipo de instância EC2 para os brokers do Kafka"
  type        = string
  default     = "kafka.m5.large"
}

# -----------------------
# Redshift
# -----------------------
variable "redshift_node_type" {
  description = "Tipo de nó Redshift"
  type        = string
  default     = "dc2.large"
}

variable "redshift_nodes" {
  description = "Número de nós Redshift"
  type        = number
  default     = 2
}

variable "redshift_master_user" {
  description = "Usuário administrador do Redshift"
  type        = string
  default     = "adminuser"
}

variable "redshift_master_password" {
  description = "Senha do usuário administrador Redshift"
  type        = string
  sensitive   = true
}

# -----------------------
# DMS
# -----------------------
variable "dms_instance_class" {
  description = "Classe de instância para o replication instance do DMS"
  type        = string
  default     = "dms.t3.medium"
}

variable "dms_storage" {
  description = "Tamanho em GB do storage alocado para DMS"
  type        = number
  default     = 50
}

# -----------------------
# Lambda
# -----------------------
variable "lambda_runtime" {
  description = "Runtime da função Lambda"
  type        = string
  default     = "python3.9"
}

variable "lambda_handler" {
  description = "Handler da função Lambda"
  type        = string
  default     = "lambda_function.lambda_handler"
}

variable "lambda_filename" {
  description = "Caminho do pacote ZIP da função Lambda"
  type        = string
  default     = "lambda.zip"
}

# -----------------------
# CodePipeline / CodeBuild / CodeDeploy
# -----------------------
variable "pipeline_source_bucket" {
  description = "Bucket de origem para o CodePipeline (opcional se usar outro source)"
  type        = string
  default     = ""
}

variable "pipeline_source_object" {
  description = "Objeto origem (zip) para o CodePipeline"
  type        = string
  default     = "source.zip"
}

# -----------------------
# Tags padrão
# -----------------------
variable "default_tags" {
  description = "Mapa de tags padrão"
  type        = map(string)
  default = {
    Owner       = "DataEng"
    ManagedBy   = "Terraform"
  }
}
