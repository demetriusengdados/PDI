from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, to_json, struct
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Criar SparkSession
spark = (
    SparkSession.builder
    .appName("IcebergKafkaIncremental")
    .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.spark_catalog.type", "hive")
    .config("spark.sql.catalog.spark_catalog.uri", "thrift://localhost:9083")
    .getOrCreate()
)

# Schema dos dados
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("nome", StringType(), True),
    StructField("email", StringType(), True)
])

# ----------------------------
# 1) Iceberg → Kafka (Incremental)
# ----------------------------
iceberg_df = (
    spark.readStream
    .format("iceberg")
    .option("stream-from-timestamp", "2025-08-10T00:00:00")  # ou usar snapshot-id
    .table("spark_catalog.db_name.iceberg_table")
)

(
    iceberg_df
    .selectExpr("CAST(id AS STRING) AS key")
    .withColumn("value", to_json(struct("*")))
    .writeStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("topic", "usuarios_topic")
    .option("checkpointLocation", "/tmp/chk/iceberg_to_kafka")
    .start()
)

# ----------------------------
# 2) Kafka → Iceberg (Incremental)
# ----------------------------
kafka_stream_df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "usuarios_topic")
    .option("startingOffsets", "earliest")
    .load()
)

parsed_df = (
    kafka_stream_df
    .selectExpr("CAST(value AS STRING)")
    .select(from_json(col("value"), schema).alias("data"))
    .select("data.*")
)

(
    parsed_df
    .writeStream
    .format("iceberg")
    .outputMode("append")
    .option("path", "spark_catalog.db_name.iceberg_table")
    .option("checkpointLocation", "/tmp/chk/kafka_to_iceberg")
    .start()
)

spark.streams.awaitAnyTermination()
