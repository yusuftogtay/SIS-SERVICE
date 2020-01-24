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
        try:
            if self.db.is_connected():
                print("Connection successful")
                print("Connected server:" + conf.mysqlHost())
                print("Connected Port: " + conf.mysqlPort())
                print("Connected Database: " + conf.mysqlDb())
        except:
            print("Connection failed")
            self.db.ping(reconnect=True, attempts=1, delay=5)

    def getActiveHubList(self):
        """
        :return: <list>
        """
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT DEVICE_ID FROM DEVICE_STOCK WHERE DEVICE_TYPE = 'HUB'")
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

    def insertWsSensorData(self ,**kwargs):
        deviceID = kwargs.get('DeviceID', None)
        airQuality = kwargs.get('airQuality', None)
        airTemperature = kwargs.get('airTemperature', None)
        airHumidity = kwargs.get('aitHumidity', None)
        rain = kwargs.get('rain', None)
        sendTime = kwargs.get('sendTime', None)
        self.db.connect()
        cursor = self.db.cursor()
        sql = "INSERT INTO WS_SENS_STATUS VALUES (%s,%s,%s,%s,%s,%s)"
        values = (deviceID,airQuality,airTemperature,airHumidity,rain,sendTime)
        cursor.execute(sql, values)
        self.db.commit()
        print("Inserted: ", cursor.lastrowid)
        cursor.close()

    def insertSmSensorData(self,**kwargs):
        deviceID = kwargs.get('DeviceID', None)
        s3 = kwargs.get('s3', None)
        s6 = kwargs.get('s6', None)
        s9 = kwargs.get('s9', None)
        downTemperature = kwargs.get('downTemperature', None)
        upTemperature = kwargs.get('upTemperature', None)
        sendTime = kwargs.get('sendTime', None)
        cursor = self.db.cursor()
        sql = "INSERT INTO SM_SENS_STATUS VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (deviceID, s3, s6, s9, downTemperature, upTemperature, sendTime)
        cursor.execute(sql,values)
        self.db.commit()
        print("Inserted: ", cursor.lastrowid)
        cursor.close()




