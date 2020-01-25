import json

with open("package.json") as jsonFile:
    data = json.load(jsonFile)


def getMqttHost():
    """
    :return: <list>
    """
    host = data["connect"]["mqtt"]["MQTT_HOST"]
    return host


def getMqttPort():
    """
        :return: <list>
    """
    port = data["connect"]["mqtt"]["MQTT_PORT"]
    port = int(port)
    return port


def getMqttUserName():
    """
        :return: <list>
    """
    userName = data["connect"]["mqtt"]["MQTT_USERNAME"]
    return userName


def getMqttPassword():
    """
        :return: <list>
    """
    password = data["connect"]["mqtt"]["MQTT_PASSWORD"]
    return password


def getMqttKeepAlive():
    """
        :return: <list>
    """
    keepalive = data["connect"]["mqtt"]["MQTT_KEEPALIVE"]
    keep = int(keepalive)
    return keep


def getMysqlHost():
    """
        :return: <list>
    """
    host = data["connect"]["mysql"]["MYSQL_HOST"]
    return host


def getMysqlPort():
    """
        :return: <list>
    """
    port = data["connect"]["mysql"]["MYSQL_PORT"]
    return port


def getMysqlUserName():
    """
        :return: <list>
    """
    userName = data["connect"]["mysql"]["MYSQL_USERNAME"]
    return userName


def getMysqlPassword():
    """
        :return: <list>
    """
    password = data["connect"]["mysql"]["MYSQL_PASSWORD"]
    return password


def getMysqlDb():
    """
        :return: <list>
    """
    keepalive = data["connect"]["mysql"]["MYSQL_DATABASE"]
    return keepalive


def getTopics():
    top1 = data["topics"]["data"]
    top2 = data["topics"]["status"]
    top3 = data["topics"]["info"]
    topics = (top1, top2, top3)
    return topics
