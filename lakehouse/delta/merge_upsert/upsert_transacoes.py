# notebooks/merge/upsert_transacoes.py

from delta.tables import DeltaTable

path = "/mnt/silver/transacoes/"
df_novos_dados = spark.read.json("/mnt/stream/novas_transacoes/")

deltaTable = DeltaTable.forPath(spark, path)

(
    deltaTable.alias("target")
    .merge(
        df_novos_dados.alias("source"),
        "target.id_transacao = source.id_transacao"
    )
    .whenMatchedUpdateAll()
    .whenNotMatchedInsertAll()
    .execute()
)
