from dbConnect import Connect


def cleanDeviceID(devices):
    cleandevices = list()
    for i in devices:
        for x in i:
            cleandevices.append(str(x))
    return cleandevices



class Device(object):
    # Constructor
    def __init__(self):
        self.db = Connect()

    def getActivateHub(self):
        return cleanDeviceID(devices=self.db.getActiveHubList())

    def getActivateChildSensor(self,activehubs):
        return cleanDeviceID(devices=self.db.getChildSensorList(ParentID=activehubs))

    def getDeviceMessageType(self,topic):
        messageType = topic.split("/")
        return messageType.index(-1)

    def getDeviceMessageID(self,topic):
        deviceID = topic.split("/")
        if len(deviceID) == 2:
            return deviceID.index(-2)
        elif len(deviceID) == 3:
            return deviceID.index(1)