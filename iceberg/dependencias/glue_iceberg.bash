spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog

spark.sql.catalog.glue_catalog.warehouse=s3://my-iceberg-lake/iceberg/

spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog

spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO

spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions