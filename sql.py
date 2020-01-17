import mysql.connector




def deviceStockExtraction():
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
    global hubDeviceList
    hubDeviceList = set()
    global smDeviceList
    smDeviceList = set()
    global wsDeviceList
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


def createTopic(deviceID="",topicname=""):
    ID = str(deviceID)
    createTopic = ID + "/" + topicname
    return createTopic





