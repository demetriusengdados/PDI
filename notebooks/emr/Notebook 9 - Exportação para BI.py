'''// Notebook 9 - Exportação para BI (Parquet ou CSV)'''
df = spark.read.format("hudi").load("s3://gold/indicadores_produto")
df.write.mode("overwrite").option("header", True).csv("s3://export/indicadores_produto")