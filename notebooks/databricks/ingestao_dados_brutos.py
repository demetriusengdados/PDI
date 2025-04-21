'''============================
// NOTEBOOKS PARA DATABRICKS
// ============================

// Notebook 1 - Ingestão de dados brutos (Kafka -> Bronze)
// Databricks'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

schema = StructType().add("produto_id", StringType()) \
                        .add("nome", StringType()) \
                        .add("preco", DoubleType())

spark = SparkSession.builder.appName("IngestaoKafka").getOrCreate()
df = spark.readStream.format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:9092") \
        .option("subscribe", "produtos") \
        .load()

json_df = df.select(from_json(col("value"), schema).alias("data")).select("data.*")

json_df.writeStream \
    .format("delta") \
    .option("checkpointLocation", "/mnt/bronze/checkpoints/produtos") \
    .outputMode("append") \
    .start("/mnt/bronze/produtos")
