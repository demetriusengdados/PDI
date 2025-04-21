# notebooks/bronze/ingest_raw_transacoes_iceberg.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

# Configurações Iceberg
spark = SparkSession.builder.appName("IcebergLakehouse").getOrCreate()
spark.conf.set("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkCatalog")
spark.conf.set("spark.sql.catalog.spark_catalog.type", "hive")
spark.conf.set("spark.sql.catalog.spark_catalog.warehouse", "/mnt/iceberg/warehouse")

# Lê os dados raw (JSON, CSV, ou de um tópico Kafka)
df_raw = spark.read.json("/mnt/raw/transacoes/")

# Adiciona timestamp de ingestão
df_bronze = df_raw.withColumn("dh_ingestao", current_timestamp())

# Escreve os dados no formato Iceberg na camada Bronze
df_bronze.write.format("iceberg") \
    .mode("append") \
    .save("spark_catalog.default.transacoes_bronze")
