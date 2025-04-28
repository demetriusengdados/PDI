import time
import json
from datetime import datetime

def simular_dados_iot():
    """Simula a leitura de dados de um dispositivo IoT."""
    temperatura = 25 + (time.time() % 10)
    umidade = 60 + (time.time() % 5)
    return {"temperatura": round(temperatura, 2), "umidade": round(umidade, 2), "timestamp": datetime.now().isoformat()}

def processar_dados(dados):
    """Realiza algum processamento nos dados recebidos."""
    print(f"Dados brutos recebidos: {dados}")
    temperatura_celsius = dados.get("temperatura")
    umidade_percentual = dados.get("umidade")

    if temperatura_celsius is not None and umidade_percentual is not None:
        if temperatura_celsius > 30:
            print("Alerta: Temperatura alta!")
        if umidade_percentual < 50:
            print("Aviso: Umidade baixa.")

        dados_processados = {
            "temperatura_celsius": temperatura_celsius,
            "umidade_percentual": umidade_percentual,
            "timestamp": dados.get("timestamp")
        }
        print(f"Dados processados: {dados_processados}")
        return json.dumps(dados_processados)
    else:
        print("Erro: Dados incompletos.")
        return None

def enviar_para_nuvem(dados_json):
    """Simula o envio dos dados processados para a nuvem (ex: Azure IoT Hub, AWS IoT Core)."""
    if dados_json:
        print(f"Enviando para a nuvem: {dados_json}")
        # Aqui você usaria bibliotecas como 'azure-iot-device' ou 'awsiotsdk'
        # para enviar os dados para a plataforma de nuvem IoT.
    else:
        print("Nenhum dado para enviar para a nuvem.")

if __name__ == "__main__":
    while True:
        dados_iot = simular_dados_iot()
        dados_processados_json = processar_dados(dados_iot)
        enviar_para_nuvem(dados_processados_json)
        time.sleep(5)