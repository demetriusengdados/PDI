import ssl
from paho.mqtt.client import Client as AWSClient

def enviar_para_aws(dados_json, endpoint, port, cert_path, key_path, root_ca_path, topic):
    try:
        client = AWSClient()
        client.tls_set(ca_certs=root_ca_path,
                       certfile=cert_path,
                       keyfile=key_path,
                       tls_version=ssl.PROTOCOL_TLSv1_2)
        client.connect(endpoint, port)
        client.loop_start()
        client.publish(topic, dados_json)
        print("Dados enviados para AWS IoT Core.")
        client.loop_stop()
    except Exception as e:
        print(f"Erro AWS: {e}")
