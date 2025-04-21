'''// Notebook 7 - Agregações por tempo (trailing 7 dias)'''
from pyspark.sql.functions import window

df = spark.read.format("delta").load("/mnt/silver/transacoes")

df.groupBy(window("dh_transacao", "7 days"), "produto_id") \
    .agg(sum("quantidade").alias("qtd")) \
    .write.format("delta").mode("overwrite") \
    .save("/mnt/gold/indicadores_7dias")