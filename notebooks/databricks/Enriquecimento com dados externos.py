'''// Notebook 3 - Enriquecimento com dados externos'''
from pyspark.sql.functions import lit, current_timestamp

df_silver = spark.read.format("delta").load("/mnt/silver/produtos")
df_categoria = spark.read.csv("/mnt/raw/categorias.csv", header=True)

joined = df_silver.join(df_categoria, "produto_id", "left")
joined = joined.withColumn("dh_processamento", current_timestamp())

joined.write.format("delta").mode("overwrite").save("/mnt/gold/produtos")