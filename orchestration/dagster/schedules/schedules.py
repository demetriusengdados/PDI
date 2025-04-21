from dagster import ScheduleDefinition
from ..jobs.ingest_job import ingest_job
from ..jobs.validation_job import validation_job

ingest_schedule = ScheduleDefinition(job=ingest_job, cron_schedule="0 * * * *")  # hourly
validation_schedule = ScheduleDefinition(job=validation_job, cron_schedule="0 6 * * *")  # daily 6am
