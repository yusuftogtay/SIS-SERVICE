import mysql.connector
from configure import Configure


class Connect(object):

    def __init__(self):
        self.mysqlHost = Configure.getMysqlHost
        self.mysqlPort = Configure.getMysqlPort
        self.mysqlUsername = Configure.getMysqlUserName
        self.mysqlPassword = Configure.getMysqlPassword
        self.mysqlDb = Configure.getMysqlDb
        self.db = mysql.connector.connect(
            host=self.mysqlHost,
            user=self.mysqlUsername,
            passwd=self.mysqlPassword,
            database=self.mysqlDb,
            port=self.mysqlPort
        )
        if self.db.is_connected():
            print("Connection successful")
            print("Connected server:" + Configure.getMysqlHost)
            print("Connected Port: " + Configure.getMysqlPort)
            print("Connected Database: " + Configure.getMysqlDb)
        else:
            self.db.ping(reconnect=True, attempts=1, delay=5)
        self.queryHubData = "INSERT INTO HUB_DATA VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.queryHubInfo = "INSERT INTO HUB_INFO VALUES (%s, %s, %s, %s, %s)"
        self.queryHubStatus = "INSERT INTO HUB_STATUS VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.querySensStatus = "INSERT INTO HUB_INFO VALUES (%s, %s, %s, %s, %s)"
        self.querySoilMoistureSensorData = "INSERT INTO SOIL_MOISTURE_DATA VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.queryWeatherStationData = "INSERT INTO WEATHER_STATION_DATA VALUES (%s, %s, %s, %s, %s, %s)"
        self.queryChildSensorId = "SELECT CHILDSENSOR_ID FROM deviceparent WHERE DEVICE_ID ="
        self.queryActiveHubList = "SELECT DEVICE_ID FROM DEVICE_STOCK WHERE DEVICE_TYPE = 'HUB'"
        self.queryDeviceType = "SELECT * FROM DEVICE_STOCK"

    def getActiveHubList(self):
        """
        * Returns the list of actively working hub devices.

        :return: <list>
        """
        cursor = self.db.cursor()
        cursor.execute(self.queryActiveHubList)
        result = cursor.fetchall()
        return result

    def getDeviceType(self):
        """
        *Returns the IDs and device types of active devices from the database.

        :return: list
        """
        cursor = self.db.cursor()
        cursor.execute(self.queryDeviceType)
        result = cursor.fetchall()
        return result

    def getChildSensorList(self, **kwargs):
        """
        * Returns the list of child sensors connected to the Hub device whose id is given as a parameter.

        :param kwargs: int parentId
        :return: list
        """
        parentID = kwargs.get("ParentID", None)
        cursor = self.db.cursor()
        cursor.execute(self.queryChildSensorId + parentID)
        result = cursor.fetchall()
        cursor.close()
        return result

    # noinspection PyGlobalUndefined
    def insertIotMessage(self, deviceId, messageType, values):
        """
        *Messages from iot network are transferred to sql database with this method
        **Device type is learned by querying the incoming device id in the SQL database.
        ***Messages are filtered and added to the database according to the topics
        that device types will publish messages.

        :param values: Tuple
        :param deviceId: Int
        :param messageType: String
        """
        cursor = self.db.cursor()
        deviceTypeList = self.getDeviceType()
        global deviceType
        global query
        for devices in deviceTypeList:
            if devices[0] == deviceId:
                deviceType = devices[1]

        if deviceType == 'HUB':
            if messageType == 'Data':
                query = self.queryHubData

            elif messageType == 'Info':
                query = self.queryHubInfo

            elif messageType == 'Status':
                query = self.queryHubStatus

        elif deviceType == 'WS':
            if messageType == 'Status':
                query = self.querySensStatus

            elif messageType == 'Data':
                query = self.queryWeatherStationData

        elif deviceType == "SM":
            if messageType == 'Status':
                query = self.querySensStatus

            elif messageType == 'Data':
                query = self.queryWeatherStationData
        cursor.execute(query, values)
        lastRowId = cursor.lastrowid()
        print('Inserted: ' + lastRowId)
        cursor.close()
