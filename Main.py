import sql
import mqttSubscriber

sql.deviceStockExtraction()
mqttSubscriber.connectMQTT()
mqttSubscriber.topicDefinition()


while True:
    mqttSubscriber.subscribe()