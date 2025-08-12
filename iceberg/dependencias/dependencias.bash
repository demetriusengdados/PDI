spark-shell \
  --packages org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.4.2 \
  --conf spark.sql.catalog.spark_catalog=org.apache.iceberg.spark.SparkSessionCatalog \
  --conf spark.sql.catalog.spark_catalog.type=hive \
  --conf spark.sql.catalog.spark_catalog.uri=thrift://localhost:9083
  --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
  --conf spark.sql.warehouse.dir=/user/hive/warehouse
  --conf spark.hadoop.hive.metastore.uris=thrift://localhost:9083
  --conf spark.hadoop.hive.metastore.warehouse.dir=/user/hive/warehouse
  --conf spark.hadoop.fs.defaultFS=hdfs://localhost:9000