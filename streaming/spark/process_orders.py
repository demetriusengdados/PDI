from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .appName("Process Orders Stream") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("subscribe", "vendas.pedidos") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

json_df.writeStream \
    .format("delta") \
    .option("checkpointLocation", "/mnt/checkpoints/pedidos") \
    .start("/mnt/lakehouse/vendas/pedidos")
