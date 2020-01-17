import paho.mqtt.client as mqtt
import mysql.connector
import json


def on_connect(client, obj, rc):
    #print("rc: " +str(rc))
    pass
def on_message(client, obj, msg):
    message = msg.patload
    messageTopic = msg.topic
    messageTopicSplit = messageTopic.split("/")
    if len(messageTopicSplit) == 2:
        deviceIDHUB = messageTopic[1]
        deviceData = messageTopic[2]
    elif len(messageTopicSplit) ==3:
        deviceIDHUB = messageTopic[1]
        deviceIDSensor = messageTopic[2]
        deviceData = messageTopic[3]
        

def om_publish(client, obj, mid):
    #print("mid: " + str(mid))
    pass
def on_subscribe(client, obj, mid, granted_qos):
    #print("Subscribed: " + str(mid) + " " + str(granted_qos))
    pass
def on_log(client, obj, level,string):
    pass


mqttClient = mqtt.Client("SIS-ADMIN")
mqttClient.connect(host="185.207.37.66", port=1883, keepalive=60)
mqttClient.on_subscribe = on_subscribe
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.on_log = on_log

database = mysql.connector.connect(
        host="185.207.37.66",
        user="joseph",
        passwd="Joseph_99",
        port="3306",
        database="sis"
    )
deviceListCursor = database.cursor()
deviceListCursor.execute("SELECT DEVICE_ID FROM DEVICE_STOCK")
resultDeviceList = deviceListCursor.fetchall()
hubDeviceList = set()
smDeviceList = set()
wsDeviceList = set()
for value in resultDeviceList:
    stringValue = str(value)
    deviceID = stringValue[1:-2]
    deviceType = deviceID[6:8]
    if deviceType == "01":
        hubDeviceList.add(deviceID)
    elif deviceType == "02":
        smDeviceList.add(deviceID)
    elif deviceType == "03":
        wsDeviceList.add(deviceID)
data = "Data"
status = "status"
info = "Info"
topiclist = [data,status,info]
topic = str()
topics = set()
def createTopic(deviceID="",topicname=""):
    ID = str(deviceID)
    topic = ID + "/" + topicname
    topics.add(topic)
createTopic()
for x in topics:
    mqttClient.subscribe(x, 2)
rc = 0
while rc == 0:
    rc = mqttClient.loop()
print("rc: " + str(rc))