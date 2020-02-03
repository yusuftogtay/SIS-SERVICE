from dbConnect import Connect


def cleanDeviceID(devices):
    """
    This function makes the data from the sql query operable.

    :param devices: <list>
    :return:
    """
    cleanDevices = list()
    for i in devices:
        for x in i:
            cleanDevices.append(str(x))
    return cleanDevices


class Device(object):
    # Constructor
    def __init__(self):
        self.db = Connect()

    def getActivateHub(self):
        """
        Returns the list of hub devices enabled with CRM.

        :return cleanDeviceID(db.getActiveHubList):
        """
        return cleanDeviceID(devices=self.db.getActiveHubList())

    def getActivateChildSensor(self, activeHubs):
        """
        List child sensors connected to active hub devices.

        :param activeHubs:
        :return cleanDeviceID(db.getActiveChildSensorList):
        """
        return cleanDeviceID(devices=self.db.getChildSensorList(ParentID=activeHubs))

    @staticmethod
    def getDeviceMessageType(topic):
        """
        Returns topics posted by the device.

        :param topic:
        :return:
        """
        messageType = topic.split("/")
        return messageType[-1]

    @staticmethod
    def getDeviceMessageID(topic):
        """
        Returns the ID of the devices that published messages.

        :param topic:
        :return:
        """
        deviceID = topic.split("/")
        if len(deviceID) == 2:
            return deviceID[0]
        elif len(deviceID) == 3:
            return deviceID[1]
