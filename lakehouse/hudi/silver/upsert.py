# notebooks/silver/upsert_transacoes_hudi.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp
from pyspark.sql import DataFrame

# Configurações Hudi
hudi_options = {
    'hoodie.table.name': 'transacoes',
    'hoodie.datasource.write.recordkey.field': 'id_transacao',
    'hoodie.datasource.write.partitionpath.field': 'data_transacao',
    'hoodie.datasource.write.precombine.field': 'data_transacao',
    'hoodie.datasource.write.operation': 'upsert',
    'hoodie.datasource.write.table.name': 'transacoes',
    'hoodie.datasource.write.hive_style.partitioning': 'true'
}

# Lê os dados raw (novos dados para atualização)
df_novos_dados = spark.read.json("/mnt/stream/novas_transacoes/")

# Limpeza e validação
df_silver = df_novos_dados \
    .filter(col("valor").isNotNull() & (col("valor") >= 0)) \
    .withColumn("data_transacao", to_timestamp("data_transacao")) \
    .dropDuplicates(["id_transacao"])

# Escreve dados com Upsert (Merge)
df_silver.write.format("hudi") \
    .options(**hudi_options) \
    .mode("append") \
    .save("/mnt/hudi/transacoes/")
