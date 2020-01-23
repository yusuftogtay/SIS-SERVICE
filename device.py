import dbConnect

class device(object):
    #Constructor
    def __init__(self):
        device.deviceStock(self)


    def cleanDeviceID(self, devices):
        cleandevices = list()
        for i in devices:
            cleandevices.append(i[1,-2])
        return cleandevices


    def deviceStock(self):
        db = dbConnect.connect()
        devices = db.activeDevicelist()
        device.cleanDeviceID(self,devices=devices)