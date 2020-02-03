from ıotConnect import Iot
from device import Device
from threading import Thread as th


if __name__ == '__main__':
    mqtt = Iot()
    mqtt.setSubscribe()
    mqtt.loop()


