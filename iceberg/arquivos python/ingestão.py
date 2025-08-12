from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json

# Criar SparkSession
spark = SparkSession.builder \
    .appName("IcebergKafkaIntegration") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.spark_catalog.type", "hive") \
    .config("spark.sql.catalog.spark_catalog.uri", "thrift://localhost:9083") \
    .getOrCreate()

# Definir o schema esperado (ajuste conforme necessário)
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("nome", StringType(), True),
    StructField("email", StringType(), True)
])

# ----------------------------
# 1) Lendo dados da tabela Iceberg e enviando para Kafka
# ----------------------------
df = spark.read.table("spark_catalog.db_name.iceberg_table")

df.selectExpr("CAST(id AS STRING) AS key", "to_json(struct(*)) AS value") \
    .write \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "usuarios_topic") \
    .save()

# ----------------------------
# 2) Lendo dados do Kafka e escrevendo na tabela Iceberg
# ----------------------------
kafka_df = spark.read \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "usuarios_topic") \
    .load()

kafka_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*") \
    .writeTo("spark_catalog.db_name.iceberg_table") \
    .append()

# ----------------------------
# 3) Lendo novamente da Iceberg e mandando para Kafka (loop reverso)
# ----------------------------
df_back = spark.read.table("spark_catalog.db_name.iceberg_table")

df_back.selectExpr("CAST(id AS STRING) AS key", "to_json(struct(*)) AS value") \
    .write \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "usuarios_topic_retorno") \
    .save()
