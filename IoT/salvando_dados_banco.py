import json
import sqlite3
from datetime import datetime
import paho.mqtt.client as mqtt

# Conexão com banco SQLite
conn = sqlite3.connect("dados_iot.db", check_same_thread=False)
cursor = conn.cursor()

# Criação da tabela (executa apenas se não existir)
cursor.execute("""
CREATE TABLE IF NOT EXISTS leitura_iot (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperatura REAL,
    umidade REAL,
    timestamp_dispositivo TEXT,
    recebido_na_nuvem TEXT
)
""")
conn.commit()

def salvar_no_banco(dados):
    """Insere os dados no banco SQLite."""
    cursor.execute("""
        INSERT INTO leitura_iot (temperatura, umidade, timestamp_dispositivo, recebido_na_nuvem)
        VALUES (?, ?, ?, ?)
    """, (
        dados["temperatura_celsius"],
        dados["umidade_percentual"],
        dados["timestamp"],
        dados["recebido_na_nuvem"]
    ))
    conn.commit()
    print(f"✔️ Dados inseridos no banco: {dados}")

def processar_na_nuvem(dados_json):
    """Processa e salva os dados na nuvem (banco)."""
    dados = json.loads(dados_json)
    dados["recebido_na_nuvem"] = datetime.now().isoformat()
    salvar_no_banco(dados)

# MQTT - Recebe mensagens
def on_message(client, userdata, msg):
    print(f"📩 Dados recebidos no tópico {msg.topic}")
    processar_na_nuvem(msg.payload.decode())

# Configuração do cliente MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("iot/dispositivo1/dados")

print("📡 Aguardando dados MQTT...")
client.loop_forever()
