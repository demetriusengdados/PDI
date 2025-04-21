# notebooks/gold/aggregated_transacoes_hudi.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, col

# Lê a tabela Hudi existente (Silver)
df_silver = spark.read.format("hudi").load("/mnt/hudi/transacoes/")

# Agrega os dados
df_gold = df_silver.groupBy("id_cliente").agg(
    count("*").alias("qtde_transacoes"),
    sum("valor").alias("valor_total")
)

# Salva na camada gold (Hudi)
df_gold.write.format("hudi") \
    .options(**hudi_options) \
    .mode("overwrite") \
    .save("/mnt/hudi/transacoes_gold/")
