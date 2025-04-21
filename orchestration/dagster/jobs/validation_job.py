from dagster import define_asset_job
from ..assets.validate_pedidos import validate_pedidos

validation_job = define_asset_job(name="validation_job")
