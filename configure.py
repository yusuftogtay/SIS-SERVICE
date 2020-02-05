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
    @staticmethod
    def getMqttHost():
        """
        :return: <list>
        """
        host = data["connect"]["mqtt"]["MQTT_HOST"]
        return host

    @staticmethod
    def getMqttPort():
        """
            :return: <list>
        """
        port = data["connect"]["mqtt"]["MQTT_PORT"]
        port = int(port)
        return port

    @staticmethod
    def getMqttUserName():
        """
            :return: <list>
        """
        userName = data["connect"]["mqtt"]["MQTT_USERNAME"]
        return userName

    @staticmethod
    def getMqttPassword():
        """
            :return: <list>
        """
        password = data["connect"]["mqtt"]["MQTT_PASSWORD"]
        return password

    @staticmethod
    def getMqttKeepAlive():
        """
            :return: <list>
        """
        keepalive = data["connect"]["mqtt"]["MQTT_KEEPALIVE"]
        keep = int(keepalive)
        return keep

    @staticmethod
    def getMysqlHost():
        """
            :return: <list>
        """
        host = data["connect"]["mysql"]["MYSQL_HOST"]
        return host

    @staticmethod
    def getMysqlPort():
        """
            :return: <list>
        """
        port = data["connect"]["mysql"]["MYSQL_PORT"]
        return port

    @staticmethod
    def getMysqlUserName():
        """
            :return: <list>
        """
        userName = data["connect"]["mysql"]["MYSQL_USERNAME"]
        return userName

    @staticmethod
    def getMysqlPassword():
        """
            :return: <list>
        """
        password = data["connect"]["mysql"]["MYSQL_PASSWORD"]
        return password

    @staticmethod
    def getMysqlDb():
        """
            :return: <list>
        """
        keepalive = data["connect"]["mysql"]["MYSQL_DATABASE"]
        return keepalive

    @staticmethod
    def getTopics():
        top1 = data["topics"]["data"]
        top2 = data["topics"]["status"]
        top3 = data["topics"]["info"]
        topics = (top1, top2, top3)
        return topics