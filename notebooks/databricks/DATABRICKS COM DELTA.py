'''// ============================
// NOTEBOOK 10 - DATABRICKS COM DELTA
// ============================'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

spark = SparkSession.builder.appName("IngestaoDeltaDatabricks").getOrCreate()
df = spark.read.json("/mnt/raw/transacoes/")
df = df.withColumn("dh_ingestao", current_timestamp())

df.write.format("delta") \
    .mode("append") \
    .save("/mnt/bronze/transacoes")