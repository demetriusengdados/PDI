'''// Notebook 4 - Geração de indicadores de venda'''
from pyspark.sql.functions import sum, avg

df_transacoes = spark.read.format("hudi").load("s3://silver/transacoes")
indicadores = df_transacoes.groupBy("produto_id").agg(
    sum("quantidade").alias("qtd_total"),
    avg("preco_unitario").alias("preco_medio")
)
indicadores.write.format("hudi").mode("overwrite").save("s3://gold/indicadores_produto")