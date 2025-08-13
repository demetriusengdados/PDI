from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, LongType, StringType, TimestampType

schema = StructType([
  StructField("id", LongType()),
  StructField("nome", StringType()),
  StructField("email", StringType()),
  StructField("created_at", TimestampType())
])

kafka_df = spark.readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "<b-*.msk.amazonaws.com:9092>") \
  .option("subscribe", "usuarios_topic") \
  .option("startingOffsets", "latest") \
  .load()

parsed = kafka_df.selectExpr("CAST(value AS STRING) AS json") \
  .select(from_json(col("json"), schema).alias("data")) \
  .select("data.*")

# Iceberg sink em micro-batches
query = parsed.writeStream \
  .outputMode("append") \
  .option("checkpointLocation", "s3://my-iceberg-lake/checkpoints/usuarios/") \
  .foreachBatch(lambda batch_df, _: batch_df.writeTo("glue_catalog.db_name.usuarios").append()) \
  .start()

query.awaitTermination()
