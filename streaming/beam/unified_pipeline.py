'''// ============================
// UNIFIED PIPELINE COM APACHE BEAM
// ============================'''

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json

def parse_json(element):
    try:
        return json.loads(element)
    except Exception as e:
        return {}

def filtrar_validos(registro):
    return registro.get("produto_id") is not None and registro.get("preco") is not None

def enrich_data(registro):
    registro["preco_com_taxa"] = round(registro["preco"] * 1.1, 2)
    return registro

def run():
    options = PipelineOptions(
        runner='DirectRunner',  # Pode ser DataflowRunner, SparkRunner, FlinkRunner, etc.
        streaming=True,
        save_main_session=True
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | 'Ler do Kafka' >> beam.io.ReadFromKafka(
                consumer_config={
                    'bootstrap.servers': 'localhost:9092',
                    'group.id': 'beam-consumer'
                },
                topics=['produtos']
            )
            | 'Extrair valor' >> beam.Map(lambda record: record.value.decode('utf-8'))
            | 'Parse JSON' >> beam.Map(parse_json)
            | 'Filtrar registros válidos' >> beam.Filter(filtrar_validos)
            | 'Enriquecer dados' >> beam.Map(enrich_data)
            | 'Salvar no BigQuery' >> beam.io.WriteToBigQuery(
                table='meu_projeto:dataset.produtos',
                schema='produto_id:STRING, nome:STRING, preco:FLOAT, preco_com_taxa:FLOAT',
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
            )
        )

if __name__ == '__main__':
    run()
