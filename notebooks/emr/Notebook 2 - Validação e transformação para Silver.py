'''// Notebook 2 - Validação e transformação para Silver'''
from pyspark.sql.functions import col

df_bronze = spark.read.format("hudi").load("s3://bronze/produtos")
validados = df_bronze.filter(col("preco").isNotNull() & (col("preco") > 0))
validados.write.format("hudi").mode("overwrite").save("s3://silver/produtos")