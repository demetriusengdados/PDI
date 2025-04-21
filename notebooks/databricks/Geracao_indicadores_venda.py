'''// Notebook 4 - Geração de indicadores de venda'''
from pyspark.sql.functions import sum, avg

df_transacoes = spark.read.format("delta").load("/mnt/silver/transacoes")
indicadores = df_transacoes.groupBy("produto_id").agg(
    sum("quantidade").alias("qtd_total"),
    avg("preco_unitario").alias("preco_medio")
)
indicadores.write.format("delta").mode("overwrite").save("/mnt/gold/indicadores_produto")