from azure.iot.device import IoTHubDeviceClient, Message
import random, time

CONNECTION_STRING = "<sua-string-de-conexao>"
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

while True:
    temperature = round(random.uniform(60, 90), 2)
    vibration = round(random.uniform(0.1, 0.5), 2)
    msg = Message(f'{{"temperature": {temperature}, "vibration": {vibration}}}')
    client.send_message(msg)
    print("Mensagem enviada:", msg)
    time.sleep(5)
client.shutdown()
