# notebooks/maintenance/optimize_transacoes_hudi.py

# Otimiza a tabela (compactação e Z-Ordering)
spark.sql("""
    OPTIMIZE delta.`/mnt/hudi/transacoes/`
    ZORDER BY (id_cliente, data_transacao)
""")

# Realiza o Vacuum para remover arquivos antigos
spark.sql("""
    VACUUM delta.`/mnt/hudi/transacoes/` RETAIN 168 HOURS
""")
