from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'data-team',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='ingest_kafka_to_delta',
    default_args=default_args,
    schedule_interval='@hourly',
    catchup=False,
) as dag:

    spark_submit = BashOperator(
        task_id='run_spark_streaming',
        bash_command="""
        spark-submit \
            --master {{ var.value.SPARK_MASTER }} \
            --packages io.delta:delta-core_2.12:2.0.0 \
            /opt/airflow/scripts/process_orders.py
        """
    )

    spark_submit
