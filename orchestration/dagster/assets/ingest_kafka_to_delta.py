from dagster import asset
import os

@asset
def ingest_kafka_to_delta():
    spark_cmd = f"""
    spark-submit \
        --master {os.getenv("SPARK_MASTER", "local[*]")} \
        --packages io.delta:delta-core_2.12:2.0.0 \
        /opt/airflow/scripts/process_orders.py
    """
    os.system(spark_cmd)
