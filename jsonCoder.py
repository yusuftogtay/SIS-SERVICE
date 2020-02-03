import json
from dbConnect import Connect


class JsonDecode(object):
    def __init__(self):
        self.data = dict()
        self.messageDeviceID = int()
        self.messageType = str()
        self.con = Connect()

    # noinspection PyGlobalUndefined
    def messageDecode(self, message, messageType, messageDeviceID):
        """

        :param message:
        :param messageType:
        :param messageDeviceID:
        :return:
        """
        message = json.loads(message)
        jsonType = messageType
        jsonID = messageDeviceID
        deviceTypeList = self.con.getDeviceType()
        global deviceType
        for devices in deviceTypeList:
            if devices[0] == jsonID:
                deviceType = devices[1]

        if deviceType == "HUB":
            if jsonType == "Info":
                sens1 = message["sens1"]
                sens2 = message["sens2"]
                sens3 = message["sens3"]
                date = message["D"]
                time = message["T"]
                dateTime = date + " " + time
                values = (
                    messageDeviceID,
                    sens1,
                    sens2,
                    sens3,
                    dateTime
                )
                return values

            elif jsonType == "Status":
                batteryLevel = message["BL"]
                rfQuality = message["RF"]
                error = message["ERR"]
                batteryOrAdaptor = message["ACB"]
                relay = message["RS"]
                date = message["D"]
                time = message["T"]
                dateTime = date + " " + time
                values = (
                    messageDeviceID,
                    batteryLevel,
                    rfQuality,
                    error,
                    batteryOrAdaptor,
                    relay,
                    dateTime
                )
                return values

            elif jsonType == "Data":
                gpsCoordinate = message["GPS"]
                Latitude = gpsCoordinate[0]
                Longitude = gpsCoordinate[1]
                gpsHourLatitude = Latitude[0]
                gpsMinuteLatitude = Latitude[1]
                gpsDegreeLatitude = Latitude[2]
                gpsLatitude = Latitude[3]
                gpsHourLongitude = Longitude[0]
                gpsMinuteLongitude = Longitude[1]
                gpsDegreeLongitude = Longitude[2]
                gpsLongitude = Longitude[3]
                batteryLevel = message["BL"]
                error = message["ERR"]
                batteryOrAdaptor = message["ACB"]
                date = message["D"]
                time = message["T"]
                dateTime = date + " " + time
                values = (
                    messageDeviceID,
                    gpsHourLatitude,
                    gpsMinuteLatitude,
                    gpsDegreeLatitude,
                    gpsLatitude,
                    gpsHourLongitude,
                    gpsMinuteLongitude,
                    gpsDegreeLongitude,
                    gpsLongitude,
                    batteryLevel,
                    error,
                    batteryOrAdaptor,
                    dateTime
                )
                return values

        elif deviceType == "SM":
            if jsonType == "Status":
                batteryLevel = message["BL"]
                rfQuality = message["RF"]
                error = message["ERR"]
                date = message["D"]
                time = message["T"]
                dateTime = date + " " + time
                values = (
                    messageDeviceID,
                    batteryLevel,
                    rfQuality,
                    error,
                    dateTime
                )
                return values

            elif jsonType == "Data":
                soilMoisture30 = message["S3"]
                soilMoisture60 = message["S6"]
                soilMoisture90 = message["S9"]
                downTemperature = message["DT"]
                upTemperature = message["UT"]
                date = message["D"]
                time = message["T"]
                dateTime = date + " " + time
                values = (
                    messageDeviceID,
                    soilMoisture30,
                    soilMoisture60,
                    soilMoisture90,
                    downTemperature,
                    upTemperature,
                    dateTime
                )
                return values

        elif deviceType == "WS":
            if jsonType == "Status":
                batteryLevel = message["BL"]
                rfQuality = message["RF"]
                error = message["ERR"]
                date = message["D"]
                time = message["T"]
                dateTime = date + " " + time
                sql = (messageDeviceID, batteryLevel, rfQuality, error, dateTime)
                return sql

            elif jsonType == "Data":
                airQuality = message["AQ"]
                airTemperature = message["AT"]
                airHumidity = message["AH"]
                rain = message["R"]
                date = message["D"]
                time = message["T"]
                dateTime = date + " " + time
                values = (
                    messageDeviceID,
                    airQuality,
                    airTemperature,
                    airHumidity,
                    rain,
                    dateTime
                )
                return values
