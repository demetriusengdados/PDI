from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

spark = SparkSession.builder \
  .appName("IcebergIngest") \
  .config("spark.sql.catalog.glue_catalog", "org.apache.iceberg.spark.SparkCatalog") \
  .config("spark.sql.catalog.glue_catalog.warehouse", "s3://my-iceberg-lake/iceberg/") \
  .config("spark.sql.catalog.glue_catalog.catalog-impl", "org.apache.iceberg.aws.glue.GlueCatalog") \
  .config("spark.sql.catalog.glue_catalog.io-impl", "org.apache.iceberg.aws.s3.S3FileIO") \
  .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
  .getOrCreate()

# DataFrame simples
data = [(3, "Carla", "carla@example.com"), (4, "Diego", "diego@example.com")]
cols = ["id", "nome", "email"]
df = spark.createDataFrame(data, cols).withColumn("created_at", current_timestamp())

# Escrever no Iceberg
df.writeTo("glue_catalog.db_name.usuarios").append()

# Ler do Iceberg
df2 = spark.read.table("glue_catalog.db_name.usuarios")
df2.show()
# Encerrar a sessão Spark
spark.stop()    