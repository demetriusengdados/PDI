import time
import json
from datetime import datetime

ARQUIVO_DE_DADOS = "dados_industriais.json"  # Arquivo onde o sistema Profibus/Profinet escreve

def ler_dados_industriais():
    """Tenta ler os dados do arquivo gerado pelo sistema Profibus/Profinet."""
    try:
        with open(ARQUIVO_DE_DADOS, 'r') as f:
            dados = json.load(f)
            dados['timestamp_leitura'] = datetime.now().isoformat()
            return dados
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {ARQUIVO_DE_DADOS}")
        return None
    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON do arquivo: {ARQUIVO_DE_DADOS}")
        return None

def processar_dados_industriais(dados):
    """Processa os dados lidos do sistema industrial."""
    if dados:
        print(f"Dados industriais recebidos: {dados}")
        # Aqui você faria o processamento específico dos dados da sua rede Profibus/Profinet
        # Por exemplo, extrair valores de sensores, status de máquinas, etc.
        return json.dumps(dados)
    return None

def enviar_para_nuvem(dados_json):
    if dados_json:
        enviar_via_mqtt(dados_json)

        # Substitua com sua connection string real do Azure
        connection_string = "HostName=xxx.azure-devices.net;DeviceId=xxx;SharedAccessKey=xxx"
        enviar_para_azure(dados_json, connection_string)

        # Parâmetros da AWS
        endpoint = "xxxx-ats.iot.us-east-1.amazonaws.com"
        port = 8883
        cert_path = "cert.pem"
        key_path = "private.key"
        root_ca_path = "AmazonRootCA1.pem"
        topic = "industria/iot"
        enviar_para_aws(dados_json, endpoint, port, cert_path, key_path, root_ca_path, topic)
    else:
        print("Nenhum dado para enviar.")


if __name__ == "__main__":
    while True:
        dados_lidos = ler_dados_industriais()
        dados_processados_json = processar_dados_industriais(dados_lidos)
        enviar_para_nuvem(dados_processados_json)
        time.sleep(10) # Ler os dados a cada 10 segundos