'''// Notebook 2 - Validação e transformação para Silver'''
from pyspark.sql.functions import col

df_bronze = spark.read.format("delta").load("/mnt/bronze/produtos")
validados = df_bronze.filter(col("preco").isNotNull() & (col("preco") > 0))
validados.write.format("delta").mode("overwrite").save("/mnt/silver/produtos")