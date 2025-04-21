'''// Notebook 9 - Exportação para BI (Parquet ou CSV)'''
df = spark.read.format("delta").load("/mnt/gold/indicadores_produto")
df.write.mode("overwrite").option("header", True).csv("/mnt/export/indicadores_produto")