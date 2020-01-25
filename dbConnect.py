import mysql.connector
import configure as conf

class Connect(object):

    def __init__(self):
        self.mysqlHost = conf.getMysqlHost()
        self.mysqlPort = conf.getMysqlPort()
        self.mysqlUsername = conf.getMysqlUserName()
        self.mysqlPassword = conf.getMysqlPassword()
        self.mysqlDb = conf.getMysqlDb()
        self.db = mysql.connector.connect(
            host=self.mysqlHost,
            user=self.mysqlUsername,
            passwd=self.mysqlPassword,
            database=self.mysqlDb,
            port=self.mysqlPort
        )
        if self.db.is_connected():
            print("Connection successful")
            print("Connected server:" + conf.getMysqlHost())
            print("Connected Port: " + conf.getMysqlPort())
            print("Connected Database: " + conf.getMysqlDb())
        else:
            self.db.ping(reconnect= True, attempts=1,delay=5)

    def getActiveHubList(self):
        """
        :return: <list>
        """
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT DEVICE_ID FROM DEVICE_STOCK WHERE DEVICE_TYPE = 'HUB'")
        result = self.cursor.fetchall()
        return result

    def getDeviceType(self):
        """
        :return:
        """
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT * FROM DEVICE_STOCK")
        result = self.cursor.fetchall()
        return result

    def getChildSensorList(self, **kwargs):
        """
        :return: <list>
        """
        parentID = kwargs.get("ParentID", None)
        self.cursor = self.db.cursor()
        sql = "SELECT CHILDSENSOR_ID FROM deviceparent WHERE DEVICE_ID =" + parentID
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    # noinspection PyGlobalUndefined
    def insertIotMessage(self, deviceid, messagetype, values):
        cursor = self.db.cursor()
        deviceTypeList = self.getDeviceType()
        global deviceType
        for devices in deviceTypeList:
            if devices[0] == deviceid:
                deviceType = devices[1]
        if deviceType == "HUB":
            if messagetype == "Data":
                pass
            if messagetype == "Info":
                pass
            if messagetype == "Status":
                pass
        if messagetype == "Status":
            if deviceType == "SM":
                pass
            elif deviceType == "WS":
                pass
        elif messagetype == "Data":
            if deviceType == "SM":
                pass
            elif deviceType == "WS":
                pass

