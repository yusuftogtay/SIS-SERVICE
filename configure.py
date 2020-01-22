import json

with open("package.json") as jsonFile:
    data = json.load(jsonFile)

def mqttHost():
    """
    :return: <list>
    """
    host = data["connect"]["mqtt"]["MQTT_HOST"]
    print("MQTT Host " + host)
    return host


def mqttPort():
    """
        :return: <list>
    """
    port = data["connect"]["mqtt"]["MQTT_PORT"]
    print("MQTT Port: " + port)
    port = int(port)
    return port


def mqttUserName():
    """
        :return: <list>
    """
    userName = data["connect"]["mqtt"]["MQTT_USERNAME"]
    print("MQTT Username: " + userName)
    return userName


def mqttPasswd():
    """
        :return: <list>
    """
    passwd = data["connect"]["mqtt"]["MQTT_PASSWORD"]
    print("MQTT Password: " + passwd)
    return passwd


def mqttKeepAlive():
    """
        :return: <list>
    """
    keepalive = data["connect"]["mqtt"]["MQTT_KEEPALIVE"]
    print("MQTT Keepalive: ")
    keep = int(keepalive)
    return  keep


def mysqlHost():
    """
        :return: <list>
    """
    host = data["connect"]["mysql"]["MYSQL_HOST"]
    print("MYSQL Host: " + host)
    return host


def mysqlPort():
    """
        :return: <list>
    """
    port = data["connect"]["mysql"]["MYSQL_PORT"]
    print("MYSQL port: " + port)
    return port


def mysqlUserName():
    """
        :return: <list>
    """
    userName = data["connect"]["mysql"]["MYSQL_USERNAME"]
    print("MYSQL Username: " + userName)
    return userName


def mysqlPasswd():
    """
        :return: <list>
    """
    passwd = data["connect"]["mysql"]["MYSQL_PASSWORD"]
    print("MYSQL Password: " + passwd)
    return passwd


def mysqlDb():
    """
        :return: <list>
    """
    keepalive = data["connect"]["mysql"]["MYSQL_DATABASE"]
    print("MYSQL Database: " + keepalive)
    return keepalive

