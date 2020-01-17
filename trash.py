"""import paho.mqtt.client as mqtt

def on_connect(client, obj, rc):
    print("rc: " +str(rc))
def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
def om_publish(client, obj, mid):
    print("mid: " + str(mid))
def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
def on_log(client, obj, level,string):
    print(string)

mqttClient = mqtt.Client("SIS-ADMIN")
mqttClient.connect(host="185.207.37.66", port=1883, keepalive=60)
mqttClient.on_subscribe = on_subscribe
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message
mqttClient.on_log = on_log


mqttClient.subscribe("2001100101/Data", 0)
mqttClient.publish("2001100101/Data","Deneme")
rc = 0
while rc ==0:
    rc = mqttClient.loop()
print("rc: " + str(rc))"""












































"""
data = "Data"
status = "status"
info = "Info"
topiclist = [data,status,info]
topic = str()
topics = set()





def topicDefinition():
    sql.deviceStockExtraction()
    for x in sql.hubDeviceList:
        for y in topiclist:
            topic = sql.createTopic(deviceID=x,topicname=y)
            topics.add(topic)

def subscribe():
    for x in topics:
        print(x)"""