from dagster import define_asset_job
from ..assets.ingest_kafka_to_delta import ingest_kafka_to_delta

ingest_job = define_asset_job(name="ingest_job")
