from azure.iot.device import IoTHubDeviceClient

def enviar_para_azure(dados_json, connection_string):
    try:
        client = IoTHubDeviceClient.create_from_connection_string(connection_string)
        client.connect()
        client.send_message(dados_json)
        print("Dados enviados para Azure IoT Hub.")
        client.disconnect()
    except Exception as e:
        print(f"Erro Azure: {e}")
