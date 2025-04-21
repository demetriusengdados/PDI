from dagster import SensorDefinition, RunRequest, sensor
from kafka import KafkaConsumer
import os

KAFKA_TOPIC = os.getenv("KAFKA_TOPIC_PEDIDOS", "vendas.pedidos")
KAFKA_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

@sensor(job_name="ingest_job")
def kafka_pedido_sensor(context):
    try:
        consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=KAFKA_SERVERS,
            auto_offset_reset='latest',
            enable_auto_commit=False,
            group_id='dagster-sensor',
            consumer_timeout_ms=3000  # sai após 3s se não encontrar msg
        )

        for message in consumer:
            context.log.info(f"Mensagem detectada no Kafka: {message.value}")
            yield RunRequest(run_key=None, run_config={})
            return  # roda só uma vez por execução do sensor

    except Exception as e:
        context.log.error(f"Erro ao verificar Kafka: {str(e)}")
