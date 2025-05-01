import json
import time
from datetime import datetime
import paho.mqtt.client as mqtt

ARQUIVO_LOG = "dados_processados_nuvem.json"

def salvar_em_arquivo(dados_dict):
    """Salva os dados recebidos em um arquivo para simular persistência."""
    with open(ARQUIVO_LOG, "a") as f:
        f.write(json.dumps(dados_dict) + "\n")
    print(f"✔️ Dados salvos: {dados_dict}")

def processar_na_nuvem(dados_json):
    """Simula um processamento adicional na nuvem."""
    dados = json.loads(dados_json)
    dados["recebido_na_nuvem"] = datetime.now().isoformat()
    salvar_em_arquivo(dados)

# Função de callback chamada quando uma nova mensagem MQTT é recebida
def on_message(client, userdata, msg):
    print(f"📩 Mensagem recebida no tópico {msg.topic}")
    processar_na_nuvem(msg.payload.decode())

# Configura o cliente MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("iot/dispositivo1/dados")

print("🌐 Aguardando dados do dispositivo IoT...")
client.loop_forever()
# O loop_forever() mantém o cliente MQTT ativo, aguardando mensagens.
# Para enviar dados para a nuvem, você pode usar o seguinte código:

mqtt_client = mqtt.Client()
mqtt_client.connect("broker.hivemq.com", 1883, 60)
mqtt_client.loop_start()

def enviar_para_nuvem(dados_json):
    if dados_json:
        mqtt_client.publish("iot/dispositivo1/dados", dados_json)
        print(f"Enviado via MQTT: {dados_json}")
    else:
        print("Nenhum dado para enviar.")
