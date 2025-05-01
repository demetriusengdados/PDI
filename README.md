🏗️ Repositório de Arquitetura de Dados Moderna (Lakehouse, CDC e Orquestração)
Este repositório contém uma arquitetura de dados moderna e modular que cobre o ciclo completo de ingestão, transformação, armazenamento, catalogação e consumo de dados utilizando ferramentas de código aberto e cloud-ready.

📚 Sumário
📁 Estrutura do Projeto

🔧 Tecnologias Utilizadas

🚀 Fluxo de Dados

📦 Componentes do Projeto

✅ Como Subir o Projeto

👥 Contribuindo

📁 Estrutura do Projeto
.
├── airflow/                  # Orquestração de pipelines
│   ├── dags/                # DAGs de ingestão e validação
│   ├── sensors/             # Sensores customizados (ex: KafkaSensor)
│   └── init.py              # Inicialização dos DAGs
│
├── beam/                    # Pipelines unificados com Apache Beam
│   └── unified_pipeline.py
│
├── dbt/                     # Transformações analíticas e contratos de dados
│   ├── models/
│   ├── macros/
│   ├── tests/
│   └── dbt_project.yml
│
├── kafka/                   # Configurações de Kafka + Debezium
│   ├── debezium-config/     # Configuração de captura de dados (CDC)
│   └── sink-connectors/     # Connectors para S3, BigQuery, Snowflake
│
├── lakehouse/
│   ├── delta/               # Pipelines de escrita Delta Lake
│   ├── hudi/                # Pipelines de escrita Hudi
│   └── iceberg/            # Pipelines de escrita Iceberg
│
├── datahub/                 # Metadata, Lineage e Governança
│   └── ingestion/
│       └── datahub-config.yml
│
├── notebooks/
│   ├── databricks/          # Notebooks para Databricks
│   └── emr/                 # Notebooks para Spark EMR
│
├── terraform/               # Provisionamento de infraestrutura em nuvem
│   ├── aws/
│   ├── azure/
│   └── gcp/
│
├── schemas/                 # Contratos de dados em JSON Schema
│   ├── produtos.schema.json
│   └── transacoes.schema.json
│
├── .env.example             # Arquivo de exemplo para configs de ambiente
├── .gitignore
└── README.md
🔧 Tecnologias Utilizadas

Camada	Ferramentas
Ingestão	Kafka, Debezium, Kafka Connect
Processamento	Apache Spark, Apache Beam, Apache Flink
Armazenamento	Delta Lake, Apache Hudi, Apache Iceberg
Orquestração	Apache Airflow
Transformações SQL	DBT
Metadata	DataHub
Infraestrutura	Terraform
Notebook Interface	Databricks, EMR Notebooks
Contratos de Dados	JSON Schema, Data Contracts
🚀 Fluxo de Dados
CDC com Debezium: captura alterações de tabelas PostgreSQL/MySQL → envia para Kafka.

Kafka Sensor no Airflow: detecta eventos e dispara DAGs.

DAGs no Airflow: validam schema, salvam staging em Delta/Hudi/Iceberg.

Apache Beam: realiza enriquecimento e escreve no destino final (ex: BigQuery).

DBT: aplica regras de negócio, modelagem em camadas (staging → mart).

DataHub: cataloga datasets, contratos e lineage.

Infra via Terraform: tudo provisionado para AWS, Azure ou GCP.

📦 Componentes do Projeto
🧩 Airflow
init.py: inicializa DAGs com o contexto correto.

kafka_sensor.py: sensor customizado que escuta tópicos Kafka.

DAGs: ingestao_produtos.py, validacao_schema.py, etc.

⚙️ Kafka Connect
debezium-postgres-connector.json: captura CDC.

s3-sink-connector.json, bigquery-sink-connector.json: entrega em diferentes camadas de destino.

📊 DBT
Modelos: stg_produtos.sql, dim_produto.sql

Macros: funções SQL reutilizáveis.

Tests: unique, not_null, relationship, etc.

🧪 Beam Pipeline
unified_pipeline.py: leitura do Kafka, enriquecimento e gravação.

🧬 DataHub
datahub-config.yml: define ingestão de metadados para DataHub.

☁️ Terraform
Criação de buckets S3, clusters EMR, instâncias Kafka e permissões.

✅ Como Subir o Projeto
Configurar ambiente
cp .env.example .env

# preencha suas variáveis (DB, Kafka, Cloud, etc)
Subir Kafka + Debezium (local)
docker-compose -f kafka/docker-compose.yml up -d

Rodar Airflow localmente
cd airflow
docker-compose up

Deploy DataHub
datahub docker quickstart

Rodar notebooks (Databricks ou EMR)
Use os notebooks na pasta notebooks/databricks ou notebooks/emr

Executar Terraform
cd terraform/aws
terraform init && terraform apply

# 🌐 Projeto IoT Industrial com Profinet, MQTT e Armazenamento em Banco

Este projeto simula um ambiente de automação industrial com sensores conectados a uma rede **Profinet**, enviando dados para a **nuvem** via **MQTT**, e armazenando esses dados em um banco de dados local **SQLite**.

---

## 🔧 Tecnologias e Bibliotecas Usadas

- Python 3.10+
- `paho-mqtt` – Envio/recebimento de dados via MQTT
- `sqlite3` – Armazenamento local dos dados IoT
- `json`, `datetime`, `time` – Processamento e formatação
- Broker público: [HiveMQ](https://broker.hivemq.com)

---

## 📂 Estrutura

📁 projeto-iot-industrial/ ├── dispositivo_iot.py # Simula dados e envia para MQTT ├── nuvem_com_banco.py # Recebe dados MQTT e salva no SQLite ├── dados_iot.db # Banco de dados gerado ├── requirements.txt # Dependências (paho-mqtt) └── README.md

---

## ▶️ Como executar

### 1. Instale as dependências:
```bash
pip install paho-mqtt

Execute o script de nuvem (servidor):
python nuvem_com_banco.py

Em outro terminal, execute o script do dispositivo simulador:
python dispositivo_iot.py

💾 Banco de dados
Os dados são armazenados em dados_iot.db com a seguinte estrutura:

id	temperatura	umidade	timestamp_dispositivo	recebido_na_nuvem

🔜 Próximos passos
Dashboard com Streamlit para visualização em tempo real

Alertas por e-mail/Telegram

Migração para banco de dados em nuvem (PostgreSQL, MongoDB, etc.)

Integração com Azure IoT Hub e AWS IoT Core


🤝 Contribuição
Pull requests são bem-vindos! Sinta-se à vontade para colaborar.

Fork o repositório

Crie sua branch com sua feature: git checkout -b minha-feature

Commit suas mudanças: git commit -m 'feat: adiciona nova DAG de ingestão'

Push para a branch: git push origin minha-feature

Crie um Pull Request

📫 Contato
Demetrius Magela da Mata - archdataconsultoria@gmail.com