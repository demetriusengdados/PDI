# notebooks/bronze/ingest_raw_transacoes.py

from pyspark.sql.functions import current_timestamp

# Lê os dados raw (pode ser CSV, JSON ou de um tópico Kafka, por exemplo)
df_raw = spark.read.json("/mnt/raw/transacoes/")

df_bronze = df_raw.withColumn("dh_ingestao", current_timestamp())

# Salva em formato Delta na camada bronze
df_bronze.write.format("delta") \
    .mode("append") \
    .option("overwriteSchema", "true") \
    .save("/mnt/bronze/transacoes/")
