# notebooks/maintenance/optimize_transacoes.py

spark.sql("""
    OPTIMIZE delta.`/mnt/silver/transacoes/`
    ZORDER BY (id_cliente, data_transacao)
""")

spark.sql("""
    VACUUM delta.`/mnt/silver/transacoes/` RETAIN 168 HOURS
""")
