'''// Notebook 8 - Criação de tabelas Hive'''
from pyspark.sql import SparkSession
spark.sql("DROP TABLE IF EXISTS ecommerce.tbl_produto_view")
spark.sql("CREATE EXTERNAL TABLE ecommerce.tbl_produto_view STORED AS PARQUET LOCATION 's3://gold/produtos'")