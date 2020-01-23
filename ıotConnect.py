import paho.mqtt.client as mqtt
import configure

host = configure.mqttHost()
port = configure.mqttPort()
keepalive = configure.mqttKeepAlive()


def on_subscribe():
    pass
def on_connect():
    pass
def on_message():
    pass
def on_log():
    pass
def on_publish():
    pass
def on_disconnect():
    pass
def on_unsubscribe():
    pass

mqttClient = mqtt.Client("SIS_ADMIN")
mqttClient.connect(host=host, port=port, keepalive=keepalive)
mqttClient.on_message = on_message
mqttClient.on_connect = on_connect
mqttClient.on_log = on_log
mqttClient.on_publish = on_publish
mqttClient.on_subscribe = on_subscribe
mqttClient.on_disconnect = on_disconnect
mqttClient.on_unsubscribe = on_unsubscribe
