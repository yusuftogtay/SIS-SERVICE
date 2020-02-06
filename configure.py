import json

with open("package.json") as jsonFile:
    data = json.load(jsonFile)


class Colors:
    header = '\033[95m'
    okBlue = '\033[94m'
    okGreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    enDc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


class Configure:
    getMqttHost = data["connect"]["mqtt"]["MQTT_HOST"]
    getMqttPort = data["connect"]["mqtt"]["MQTT_PORT"]
    getMqttUserName = data["connect"]["mqtt"]["MQTT_USERNAME"]
    getMqttPassword = data["connect"]["mqtt"]["MQTT_PASSWORD"]
    getMqttKeepAlive = data["connect"]["mqtt"]["MQTT_KEEPALIVE"]
    getMysqlHost = data["connect"]["mysql"]["MYSQL_HOST"]
    getMysqlUserName = data["connect"]["mysql"]["MYSQL_USERNAME"]
    getMysqlPassword = data["connect"]["mysql"]["MYSQL_PASSWORD"]
    getMysqlPort = data["connect"]["mysql"]["MYSQL_PORT"]
    getMysqlDb = data["connect"]["mysql"]["DATABASE"]
    getTopics = (data["topics"]["data"], data["topics"]["status"], data["topics"]["info"])
