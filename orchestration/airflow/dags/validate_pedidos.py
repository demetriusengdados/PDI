from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'data-quality',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='validate_pedidos_ge',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    run_validation = BashOperator(
        task_id='ge_validation',
        bash_command="""
        great_expectations checkpoint run pedidos_checkpoint \
            --config-dir {{ var.value.GE_DATA_CONTEXT_ROOT_DIR }}
        """
    )

    run_validation
