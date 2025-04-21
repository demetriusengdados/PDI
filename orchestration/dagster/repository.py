
from dagster import Definitions
from .assets.ingest_kafka_to_delta import ingest_kafka_to_delta
from .assets.validate_pedidos import validate_pedidos
from .jobs.ingest_job import ingest_job
from .jobs.validation_job import validation_job
from .schedules.schedules import ingest_schedule, validation_schedule

defs = Definitions(
    assets=[ingest_kafka_to_delta, validate_pedidos],
    jobs=[ingest_job, validation_job],
    schedules=[ingest_schedule, validation_schedule],
)
