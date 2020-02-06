import paho.mqtt.client as mqtt
from configure import Configure
from configure import Colors
from device import Device
from jsonCoder import JsonDecode as deCoder
from dbConnect import Connect


class Iot:
    def __init__(self):
        self.host = Configure.getMqttHost
        self.port = Configure.getMqttPort
        self.keepalive = Configure.getMqttKeepAlive
        self.mqttClient = mqtt.Client("SIS_ADMIN")
        self.mqttClient.connect(host=self.host, port=self.port, keepalive=self.keepalive)
        self.mqttClient.on_message = self.on_message
        self.mqttClient.on_connect = self.on_connect
        self.mqttClient.on_log = self.on_log
        self.mqttClient.on_publish = self.on_publish
        self.mqttClient.on_subscribe = self.on_subscribe
        self.mqttClient.on_disconnect = self.on_disconnect
        self.mqttClient.on_unsubscribe = self.on_unsubscribe
        self.mqttClient.message_callback_add = self.messageCallBackAdd
        self.mqttClient.message_callback_remove = self.messageCallBackRemove
        self.connect = Connect()
        self.device = Device()
        self.rc = 0
        self.deviceList = list()

    def setSubscribe(self):
        subs = self.setTopic()
        for sub in subs:
            self.mqttClient.subscribe(sub)

    def loop(self):
        while self.rc == 0:
            self.rc = self.mqttClient.loop()
        print("RC: " + str(self.rc))

    def publishMessage(self, message='', topic='', qos=0):
        """
        It enables sending messages in Json format with MQTT protocol.

        :param message: Payload (In the Json format)
        :param topic: Subject to the message
        :param qos: Quality of Service 0,1 or 2
        """
        self.mqttClient.publish(topic=topic, payload=message, qos=qos, retain=False)
        pass

    def setTopic(self):
        activeHubs = self.device.getActivateHub()
        for hub in activeHubs:
            activeChildSensor = self.device.getActivateChildSensor(activeHubs=hub)
            for data in Configure.getTopics:
                topic = hub + "/" + data
                self.deviceList.append(topic)
            for child in activeChildSensor:
                for data in Configure.getTopics:
                    topic = hub + "/" + child + "/" + data
                    self.deviceList.append(topic)
        return self.deviceList

    def on_message(self, client, userdata, msg):
        """
        Called when a message has been received on a topic that the client subscribes to and the message does
        not match an existing topic filter callback. Use message_callback_add() to define a callback that will be
        called for specific topic filters. on_message will serve as fallback when none matched.

        :param client: The client instance for this callback
        :param userdata: The private user data as set in Client() or user_data_set()
        :param msg: An instance of MQTTMessage. This is a class with members topic, payload, qos, retain.
        :return:
        """
        messageType = self.device.getDeviceMessageType(msg.topic)
        deviceID = self.device.getDeviceMessageID(msg.topic)
        messagePayload = msg.payload
        parse = deCoder()
        parseMessage = parse.messageDecode(
            message=messagePayload,
            messageType=messageType,
            messageDeviceID=deviceID
        )
        self.connect.insertIotMessage(deviceId=deviceID, messageType=messageType, values=parseMessage)
        print("mesaj geldi " + str(client) + " " + str(userdata))

    def messageCallBackAdd(self, sub, callback):
        """
        This function allows you to define callbacks that handle incoming messages for specific subscription filters,
        including with wildcards. This lets you, for example, subscribe to sensors/# and have one callback to handle
        sensors/temperature and another to handle sensors/humidity.

        If using message_callback_add() and on_message, only messages that do not match a subscription
        specific filter will be passed to the on_message callback.

        If multiple sub match a topic, each callback will be called (e.g. sub sensors/# and sub +/humidity
        both match a message with a topic sensors/humidity, so both callbacks will handle this message).

        :param sub: The subscription filter to match against for this callback. Only one callback may be defined per
        literal sub string
        :param callback: The callback to be used. Takes the same form as the on_message callback
        :return:
        """
        pass

    def messageCallBackRemove(self, sub):
        """
        Remove a topic/subscription specific callback previously registered using message_callback_add().

        :param sub: The subscription filter to remove
        :return:
        """
        pass

    def on_subscribe(self, client, userdata, mid, granted_qos):
        pass

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        """
        Called when the broker responds to our connection request.
        Using clean session set to 0 only. If a client with clean session=0, that reconnects to a broker that it
        has previously connected to, this flag indicates whether the broker still has the session information
        for the client. If 1, the session still exists.

        The value of rc indicates success or not:
        0: Connection successful
        1: Connection refused - incorrect protocol version
        2: Connection refused - invalid client identifier
        3: Connection refused - server unavailable
        4: Connection refused - bad username or password
        5: Connection refused - not authorised
        6-255: Currently unused.

        :param client: The client instance for this callback
        :param userdata: The private user data as set in Client() or user_data_set()
        :param flags: Response flags sent by the broker
        :param rc: The connection result
        :return:
        """
        if rc == 0:
            print(f"{Colors.okGreen} {client} {userdata} {flags} MQTT Connection successful... {Colors.enDc}")
            print(f'{Colors.okGreen}Connection Host: {Colors.enDc}' + Configure.getMqttHost())
        elif rc == 1:
            print(f'{Colors.fail}Connection refused - incorrect protocol version. {Colors.enDc}')
            print(client + " " + userdata)
        elif rc == 2:
            print(f'{Colors.fail}Connection refused - invalid client identifier {Colors.enDc}')
            print(client + " " + userdata)
        elif rc == 3:
            print(f"{Colors.fail}Connection refused - server unavailable {Colors.enDc}")
            print(client + " " + userdata)
        elif rc == 4:
            print(f"{Colors.fail}Connection refused - bad username or password {Colors.enDc}")
            print(client + " " + userdata)
        elif rc == 5:
            print(f"{Colors.fail}Connection refused - not authorised {Colors.enDc}")
            print(client + " " + userdata)
        else:
            print(f"{Colors.fail}Currently unused. {Colors.enDc}")
            print(client + " " + userdata)

    @staticmethod
    def on_disconnect(client, userdata, rc):
        """
        Called when the client disconnects from the broker.
        The rc parameter indicates the disconnection state. If MQTT_ERR_SUCCESS (0), the callback was called in
        response to a disconnect() call. If any other value the disconnection was unexpected, such as might be
        caused by a network error.

        :param client: The client instance for this callback
        :param userdata: The private user data as set in Client() or user_data_set()
        :param rc: The disconnection result
        :return:
        """
        if rc != 0:
            print("Unexpected disconnection.")
            print(str(client) + " " + str(userdata))
            
    @staticmethod
    def on_log(client, level, buf):
        """
        Called when the client has log information. Define to allow debugging.
        Level will be one of;
        MQTT_LOG_INFO,
        MQTT_LOG_NOTICE,
        MQTT_LOG_WARNING,
        MQTT_LOG_ERR,
        MQTT_LOG_DEBUG.

        :param client: The client instance for this callback
        :param level: The level variable gives the severity of the message
        :param buf: The message itself is in buf.
        :return:
        """
        if level == "MQTT_LOG_INFO":
            print(f"{Colors.okBlue} {client} INFO : {buf}{Colors.enDc}")
        elif level == "MQTT_LOG_NOTICE":
            print(f"{Colors.okBlue} {client} NOTICE : {buf}{Colors.enDc}")
        elif level == "MQTT_LOG_WARNING":
            print(f"{Colors.warning} {client} WARNING : {buf}{Colors.underline}")
        elif level == "MQTT_LOG_ERR":
            print(f"{Colors.fail} {client} INFO : {buf}{Colors.underline}")
        elif level == "MQTT_LOG_DEBUG":
            print(f"{Colors.header} {client} INFO : {buf}{Colors.enDc}")

    @staticmethod
    def on_publish(client, userdata, mid):
        """
        Called when a message that was to be sent using the publish() call has completed transmission to the broker.
        For messages with QoS levels 1 and 2, this means that the appropriate handshakes have completed.
        For QoS 0, this simply means that the message has left the client.
        The mid variable matches the mid variable returned from the corresponding publish() call,
        to allow outgoing messages to be tracked.

        This callback is important because even if the publish() call returns success,
        it does not always mean that the message has been sent.

        :param client: The client instance for this callback
        :param userdata: The private user data as set in Client() or user_data_set()
        :param mid: The mid variable matches the mid variable returned from the corresponding publish() call,
        to allow outgoing messages to be tracked.
        :return:
        """
        print("Publish: " + str(client) + " " + str(userdata) + " " + str(mid))

    @staticmethod
    def on_unsubscribe(client, userdata, mid):
        """
        Called when the broker responds to an unsubscribe request. The mid variable matches the mid variable returned
        from the corresponding unsubscribe() call.

        :param client:
        :param userdata:
        :param mid:
        :return:
        """
        print("Client: " + client)
        print("Userdata: " + userdata)
        print("Mid: " + mid)
