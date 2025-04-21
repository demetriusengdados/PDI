from dagster import asset
import os

@asset
def validate_pedidos():
    ge_root = os.getenv("GE_DATA_CONTEXT_ROOT_DIR", "./great_expectations")
    os.system(f"great_expectations checkpoint run pedidos_checkpoint --config-dir {ge_root}")
