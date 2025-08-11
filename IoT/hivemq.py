import paho.mqtt.client as mqtt

def enviar_via_mqtt(dados_json):
    try:
        broker = "broker.hivemq.com"
        topic = "industria/iot/dados"
        client = mqtt.Client()
        client.connect(broker, 1883, 60)
        client.loop_start()
        client.publish(topic, dados_json)
        print("Dados enviados via MQTT.")
        client.loop_stop()
    except Exception as e:
        print(f"Erro MQTT: {e}")
