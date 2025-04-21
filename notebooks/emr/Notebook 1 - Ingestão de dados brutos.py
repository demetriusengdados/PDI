'''// ============================
// NOTEBOOKS PARA EMR COM HUDI (1 a 9)
// ============================

// Notebook 1 - Ingestão de dados brutos (Kafka -> Bronze)'''
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

schema = StructType().add("produto_id", StringType()) \
                        .add("nome", StringType()) \
                        .add("preco", DoubleType())

spark = SparkSession.builder \
    .appName("IngestaoKafkaEMR") \
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .getOrCreate()

df = spark.readStream.format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:9092") \
        .option("subscribe", "produtos") \
        .load()

json_df = df.select(from_json(col("value"), schema).alias("data")).select("data.*")

(json_df.writeStream \
    .format("hudi") \
    .option("checkpointLocation", "s3://bronze/checkpoints/produtos") \
    .option("hoodie.table.name", "produtos_bronze") \
    .option("hoodie.datasource.write.recordkey.field", "produto_id") \
    .option("hoodie.datasource.write.operation", "insert") \
    .option("hoodie.datasource.write.precombine.field", "preco") \
    .outputMode("append") \
    .start("s3://bronze/produtos"))
