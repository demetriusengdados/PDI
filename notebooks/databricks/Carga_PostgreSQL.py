'''// Notebook 5 - Carga em PostgreSQL para API'''
jdbc_url = "jdbc:postgresql://host:5432/data"
properties = {"user": "postgres", "password": "senha", "driver": "org.postgresql.Driver"}

spark.read.format("delta").load("/mnt/gold/indicadores_produto") \
    .write.jdbc(jdbc_url, "indicadores_produto", mode="overwrite", properties=properties)