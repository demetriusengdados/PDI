# notebooks/maintenance/optimize_transacoes_iceberg.py

# Otimiza a tabela Iceberg para compactação de arquivos pequenos
spark.sql("""
    OPTIMIZE spark_catalog.default.transacoes_silver
    ZORDER BY (id_cliente, data_transacao)
""")

# Realiza o Vacuum para remover arquivos de dados obsoletos
spark.sql("""
    VACUUM spark_catalog.default.transacoes_silver RETAIN 168 HOURS
""")
