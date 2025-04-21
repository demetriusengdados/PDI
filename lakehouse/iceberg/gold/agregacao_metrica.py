# notebooks/gold/metricas_transacoes_iceberg.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, col

# Lê os dados da camada Silver
df_silver = spark.read.format("iceberg").load("spark_catalog.default.transacoes_silver")

# Agrega os dados para gerar métricas
df_gold = df_silver.groupBy("id_cliente").agg(
    count("*").alias("qtde_transacoes"),
    sum("valor").alias("valor_total")
)

# Escreve os dados na camada Gold
df_gold.write.format("iceberg") \
    .mode("overwrite") \
    .save("spark_catalog.default.transacoes_gold")
