# notebooks/merge/upsert_transacoes_iceberg.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Lê os dados da tabela Iceberg
df_existing = spark.read.format("iceberg").load("spark_catalog.default.transacoes_silver")
df_novos_dados = spark.read.json("/mnt/stream/novas_transacoes/")

# Faz o merge dos dados existentes com os novos dados (upsert)
df_existing.createOrReplaceTempView("existing_transacoes")
df_novos_dados.createOrReplaceTempView("new_transacoes")

spark.sql("""
    MERGE INTO spark_catalog.default.transacoes_silver AS target
    USING new_transacoes AS source
    ON target.id_transacao = source.id_transacao
    WHEN MATCHED THEN
        UPDATE SET target.valor = source.valor, target.data_transacao = source.data_transacao
    WHEN NOT MATCHED THEN
        INSERT (id_transacao, id_cliente, valor, data_transacao)
        VALUES (source.id_transacao, source.id_cliente, source.valor, source.data_transacao)
""")
