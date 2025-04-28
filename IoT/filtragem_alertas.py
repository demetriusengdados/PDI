import time
import json
from datetime import datetime

LIMITE_TEMPERATURA_MAXIMA = 35
LIMITE_UMIDADE_MINIMA = 40

def simular_dados_sensor_unico():
    """Simula a leitura de dados de um sensor IoT."""
    temperatura = 22 + (random.random() * 18)
    umidade = 50 + (random.random() * 15)
    return {"temperatura": round(temperatura, 2), "umidade": round(umidade, 2), "timestamp": datetime.now().isoformat()}

def processar_dados_com_alerta(dados):
    """Verifica os dados contra limiares e gera alertas."""
    temperatura = dados.get("temperatura")
    umidade = dados.get("umidade")
    timestamp = dados.get("timestamp")
    alertas = []

    if temperatura is not None:
        if temperatura > LIMITE_TEMPERATURA_MAXIMA:
            alertas.append(f"ALERTA: Temperatura ({temperatura}°C) acima do limite ({LIMITE_TEMPERATURA_MAXIMA}°C) em {timestamp}")

    if umidade is not None:
        if umidade < LIMITE_UMIDADE_MINIMA:
            alertas.append(f"ALERTA: Umidade ({umidade}%) abaixo do limite ({LIMITE_UMIDADE_MINIMA}%) em {timestamp}")

    dados_processados = {
        "temperatura": temperatura,
        "umidade": umidade,
        "timestamp": timestamp,
        "alertas": alertas
    }
    print(f"Dados processados com alertas: {dados_processados}")
    return json.dumps(dados_processados)

def enviar_alertas(dados_json):
    """Simula o envio de dados (incluindo alertas) para a nuvem."""
    if dados_json:
        dados = json.loads(dados_json)
        if dados.get("alertas"):
            print(f"Enviando alertas para a nuvem: {dados['alertas']}")
        else:
            print("Nenhum alerta para enviar.")
        print(f"Enviando dados para a nuvem: {dados_json}")
    else:
        print("Nenhum dado para enviar.")

if __name__ == "__main__":
    while True:
        dados_sensor = simular_dados_sensor_unico()
        dados_processados_json = processar_dados_com_alerta(dados_sensor)
        enviar_alertas(dados_processados_json)
        time.sleep(3)