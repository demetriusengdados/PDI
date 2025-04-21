'''// Notebook 8 - Criação de materialized views'''
from delta.tables import DeltaTable

df = spark.read.format("delta").load("/mnt/gold/produtos")
(df.write.format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("ecommerce.tbl_produto_view"))