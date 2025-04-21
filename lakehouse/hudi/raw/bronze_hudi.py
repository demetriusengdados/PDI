# notebooks/bronze/ingest_raw_transacoes_hudi.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

# Configurações Hudi
spark = SparkSession.builder.appName("HudiLakehouse").getOrCreate()
hudi_options = {
    'hoodie.table.name': 'transacoes',
    'hoodie.datasource.write.recordkey.field': 'id_transacao',
    'hoodie.datasource.write.partitionpath.field': 'data_transacao',
    'hoodie.datasource.write.precombine.field': 'data_transacao',
    'hoodie.datasource.write.operation': 'insert',
    'hoodie.datasource.write.table.name': 'transacoes',
    'hoodie.datasource.write.hive_style.partitioning': 'true'
}

# Lê dados raw (de um CSV, Kafka ou JSON)
df_raw = spark.read.json("/mnt/raw/transacoes/")

# Adiciona timestamp de ingestão
df_bronze = df_raw.withColumn("dh_ingestao", current_timestamp())

# Escreve no Hudi (modo INSERT)
df_bronze.write.format("hudi") \
    .options(**hudi_options) \
    .mode("append") \
    .save("/mnt/hudi/transacoes/")
