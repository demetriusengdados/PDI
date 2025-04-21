'''// Notebook 3 - Enriquecimento com dados externos'''
from pyspark.sql.functions import lit, current_timestamp

df_silver = spark.read.format("hudi").load("s3://silver/produtos")
df_categoria = spark.read.csv("s3://raw/categorias.csv", header=True)

joined = df_silver.join(df_categoria, "produto_id", "left")
joined = joined.withColumn("dh_processamento", current_timestamp())

joined.write.format("hudi").mode("overwrite").save("s3://gold/produtos")