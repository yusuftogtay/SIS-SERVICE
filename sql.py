import mysql.connector

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
hubDeviceList = set()
smDeviceList = set()
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
"""for x in wsDeviceList:
    print("WS sensor id =" + x)
for y in smDeviceList:
    print("Sm sensor id =" + y)
for z in hubDeviceList:
    print("Hub device id =" +z)"""
def createTopic(deviceID="",topicname=""):
    createTopic = deviceID + "/" + topicname
    return createTopic





