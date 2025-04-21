# notebooks/gold/metricas_transacoes.py

from pyspark.sql.functions import sum, count, col

df_silver = spark.read.format("delta").load("/mnt/silver/transacoes/")

df_gold = df_silver.groupBy("id_cliente").agg(
    count("*").alias("qtde_transacoes"),
    sum("valor").alias("valor_total")
)

df_gold.write.format("delta") \
    .mode("overwrite") \
    .save("/mnt/gold/transacoes_metricas/")
