import time
import json
from datetime import datetime
import random

NUMERO_SENSORES = 30  
ARQUIVO_DE_DADOS = "dados_sensores.json"  # Arquivo onde os dados dos sensores serão armazenados

def simular_dados_multiplos_sensores():
    """Simula a leitura de dados de múltiplos sensores IoT."""
    dados_sensores = []
    for i in range(NUMERO_SENSORES):
        temperatura = 20 + (random.random() * 15)
        umidade = 55 + (random.random() * 10)
        dados_sensores.append({
            "sensor_id": f"sensor_{i+1}",
            "temperatura": round(temperatura, 2),
            "umidade": round(umidade, 2),
            "timestamp": datetime.now().isoformat()
        })
    return dados_sensores

def processar_dados_agregados(dados_sensores):
    """Calcula a média da temperatura dos sensores."""
    temperaturas = [d['temperatura'] for d in dados_sensores if 'temperatura' in d]
    if temperaturas:
        media_temperatura = sum(temperaturas) / len(temperaturas)
        dados_agregados = {
            "media_temperatura": round(media_temperatura, 2),
            "timestamp_processamento": datetime.now().isoformat(),
            "detalhes_sensores": dados_sensores
        }
        print(f"Dados agregados: {dados_agregados}")
        return json.dumps(dados_agregados)
    else:
        print("Nenhum dado de temperatura encontrado.")
        return None

def enviar_para_nuvem(dados_json):
    """Simula o envio dos dados agregados para a nuvem."""
    if dados_json:
        print(f"Enviando dados agregados para a nuvem: {dados_json}")
        # Aqui você usaria as bibliotecas de nuvem.
    else:
        print("Nenhum dado para enviar para a nuvem.")

if __name__ == "__main__":
    while True:
        dados_multiplos = simular_dados_multiplos_sensores()
        dados_agregados_json = processar_dados_agregados(dados_multiplos)
        enviar_para_nuvem(dados_agregados_json)
        time.sleep(5)