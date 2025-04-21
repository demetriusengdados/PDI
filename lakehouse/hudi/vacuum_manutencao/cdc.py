# notebooks/merge/upsert_transacoes_hudi.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

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

# Carrega dados existentes e dados novos para upsert
df_existing = spark.read.format("hudi").load("/mnt/hudi/transacoes/")
df_novos_dados = spark.read.json("/mnt/stream/novas_transacoes/")

# Faz o merge usando a chave de transação
df_existing.alias('target') \
    .merge(
        df_novos_dados.alias('source'),
        'target.id_transacao = source.id_transacao'
    ) \
    .whenMatchedUpdateAll() \
    .whenNotMatchedInsertAll() \
    .execute()
