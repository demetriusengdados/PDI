# Configuração do catálogo Iceberg para Hive
spark.conf.set("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkCatalog")
spark.conf.set("spark.sql.catalog.spark_catalog.type", "hive")
spark.conf.set("spark.sql.catalog.spark_catalog.warehouse", "/mnt/iceberg/warehouse")
