# notebooks/silver/transform_transacoes.py

from pyspark.sql.functions import col, to_timestamp

df_bronze = spark.read.format("delta").load("/mnt/bronze/transacoes/")

df_silver = df_bronze \
    .filter(col("valor").isNotNull() & (col("valor") >= 0)) \
    .withColumn("data_transacao", to_timestamp("data_transacao")) \
    .dropDuplicates(["id_transacao"])

df_silver.write.format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .save("/mnt/silver/transacoes/")
