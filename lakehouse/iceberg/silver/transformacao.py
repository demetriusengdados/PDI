# notebooks/silver/transform_transacoes_iceberg.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp

# Lê os dados da camada Bronze
df_bronze = spark.read.format("iceberg").load("spark_catalog.default.transacoes_bronze")

# Limpeza e transformação
df_silver = df_bronze.filter(col("valor").isNotNull() & (col("valor") >= 0)) \
    .withColumn("data_transacao", to_timestamp("data_transacao")) \
    .dropDuplicates(["id_transacao"])

# Escreve os dados na camada Silver
df_silver.write.format("iceberg") \
    .mode("overwrite") \
    .save("spark_catalog.default.transacoes_silver")
