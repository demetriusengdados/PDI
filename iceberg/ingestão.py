df = spark.read.table("spark_catalog.db_name.iceberg_table")

df.selectExpr("CAST(id AS STRING)", "to_json(struct(*)) AS value") \
  .write \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("topic", "usuarios_topic") \
  .save()
# Lendo dados do Kafka e escrevendo na tabela Iceberg
kafka_df = spark.read \ 
    .format("kafka") \  
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "usuarios_topic") \
    .load() 
kafka_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*") \
    .writeTo("spark_catalog.db_name.iceberg_table").append()
# Lendo dados da tabela Iceberg e escrevendo no Kafka
