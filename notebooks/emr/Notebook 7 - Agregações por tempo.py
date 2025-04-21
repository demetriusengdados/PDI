'''// Notebook 7 - Agregações por tempo (trailing 7 dias)'''
from pyspark.sql.functions import window

df = spark.read.format("hudi").load("s3://silver/transacoes")

df.groupBy(window("dh_transacao", "7 days"), "produto_id") \
    .agg(sum("quantidade").alias("qtd")) \
    .write.format("hudi").mode("overwrite") \
    .save("s3://gold/indicadores_7dias")