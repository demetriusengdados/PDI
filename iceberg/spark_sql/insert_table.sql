from pyspark.sql import SparkSession
from datetime import datetime, timedelta
import random

# Inicializa a sessão Spark
spark = SparkSession.builder \
    .appName("IcebergBulkInsert") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog") \
    .config("spark.sql.catalog.spark_catalog.type", "hive") \
    .config("spark.sql.catalog.spark_catalog.uri", "thrift://localhost:9083") \
    .getOrCreate()

# Funções auxiliares para gerar dados fictícios
def gerar_email(nome, i):
    return f"{nome.lower()}.{i}@exemplo.com"

def gerar_telefone():
    return f"+55 (31) 9{random.randint(1000,9999)}-{random.randint(1000,9999)}"

def gerar_cpf():
    return f"{random.randint(100000000,999999999):09d}"

def gerar_data_nascimento():
    return datetime(1970, 1, 1) + timedelta(days=random.randint(7000, 18000))

def gerar_endereco(i):
    return {
        "rua": f"Rua {random.choice(['A', 'B', 'C', 'D'])}{i}",
        "numero": random.randint(1, 999),
        "cidade": random.choice(["Itabira", "Belo Horizonte", "Contagem", "Uberlândia"]),
        "estado": random.choice(["MG", "SP", "RJ", "BA"]),
        "cep": f"{random.randint(30000,39999)}-{random.randint(100,999)}"
    }

# Gera dados fictícios
data = []
base_date = datetime(2025, 1, 1)

for i in range(1, 1001):
    nome = f"User_{i}"
    email = gerar_email(nome, i)
    telefone = gerar_telefone()
    cpf = gerar_cpf()
    data_nascimento = gerar_data_nascimento().date()
    data_criacao = base_date + timedelta(days=random.randint(0, 365))
    ativo = random.choice([True, False])
    saldo = round(random.uniform(0, 10000), 2)
    tipo_usuario = random.choice(["admin", "cliente", "visitante"])
    endereco = gerar_endereco(i)

    data.append((i, nome, email, telefone, cpf, data_nascimento, data_criacao.date(), ativo, saldo, tipo_usuario, endereco))

# Cria DataFrame
schema = ["id", "nome", "email", "telefone", "cpf", "data_nascimento", "data_criacao", "ativo", "saldo", "tipo_usuario", "endereco"]
df = spark.createDataFrame(data, schema)

# Insere na tabela Iceberg
df.writeTo("spark_catalog.db_name.iceberg_table").append()
