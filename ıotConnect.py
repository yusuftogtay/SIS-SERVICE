import paho.mqtt.client as mqtt
import configure as conf
from device import Device
from jsonCoder import JsonDecode as decode


class Iot:
    def __init__(self):
        self.host = conf.getMqttHost()
        self.port = conf.getMqttPort()
        self.keepalive = conf.getMqttKeepAlive()
        self.mqttClient = mqtt.Client("SIS_ADMIN")
        self.mqttClient.connect(host=self.host, port=self.port, keepalive=self.keepalive)
        self.mqttClient.on_message = self.on_message
        self.mqttClient.on_connect = self.on_connect
        self.mqttClient.on_log = self.on_log
        self.mqttClient.on_publish = self.on_publish
        self.mqttClient.on_subscribe = self.on_subscribe
        self.mqttClient.on_disconnect = self.on_disconnect
        self.mqttClient.on_unsubscribe = self.on_unsubscribe
        self.device = Device()
        self.rc = 0
        self.deviceList = list()

    def setSubscribe(self):
        subs = self.setTopic()
        for sub in subs:
            self.mqttClient.subscribe(sub)

    def loop(self):
        while self.rc == 0:
            self.rc = self.mqttClient.loop()
        print("RC: " + str(self.rc))

    def setTopic(self):
        activeHubs = self.device.getActivateHub()
        for hub in activeHubs:
            activeChildSensor = self.device.getActivateChildSensor(activehubs=hub)
            for data in conf.getTopics():
                topic = hub + "/" + data
                self.deviceList.append(topic)
            for child in activeChildSensor:
                for data in conf.getTopics():
                    topic = hub + "/" + child + "/" + data
                    self.deviceList.append(topic)
        return self.deviceList

    def on_message(self,client,userdata,msg, *args):
        messageType = self.device.getdeviceMessageType(msg.topic)
        deviceID = self.device.getdeviceMessageID(msg.topic)
        messagePayload = msg.payload
        parse = decode()
        parseMessage = parse.messageDecode(
            message=messagePayload,
            messageType=messageType,
            messageDeviceID=deviceID
        )




    def on_subscribe(self):
        pass

    def on_connect(self):
        pass

    def on_log(self):
        pass

    def on_publish(self):
        pass

    def on_disconnect(self):
        pass

    def on_unsubscribe(self):
        pass
