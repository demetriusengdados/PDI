from datahub.emitter.mce_builder import make_dataset_urn
from datahub.metadata.schema_classes import *
from datahub.emitter.rest_emitter import DatahubRestEmitter

emitter = DatahubRestEmitter(gms_server="http://localhost:8080")

dataset_urn = make_dataset_urn(platform="delta", name="clientes_gold", env="PROD")

snapshot = DatasetSnapshot(
    urn=dataset_urn,
    aspects=[
        StatusClass(removed=False),
        OwnershipClass(owners=[OwnerClass(owner="urn:li:corpuser:joao", type="DATAOWNER")]),
        DatasetPropertiesClass(description="Tabela com clientes em estágio gold"),
    ]
)

emitter.emit_mce(MetadataChangeEvent(proposedSnapshot=snapshot))
