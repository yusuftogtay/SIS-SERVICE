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


