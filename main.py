from time import sleep
import multiprocessing
import sys

class Device:
    def __init__(self, status="off"):
        self.status = status

    def switch(self):
        if self.status == "off":
            self.status = "on"
        else:
            self.status = "off"


class LightBulb(Device):
    def __init__(self, room, number=1, status="off"):
        super().__init__(status)
        self.room = room
        self.number = number


class Teapot(Device):
    def __init__(self, temperature=23.0, status="off"):
        super().__init__(status)
        self.temperature = temperature

    def get_inf(self):
        print("Температура воды в чайнике = " + str(self.temperature))

    def boil_water(self):
        while True:
            sleep(1)
            if self.status == "on":
                print("yes")
                self.temperature += 10
            else:
                self.temperature -= 1
                print(self.status)
            if self.temperature == 100:
                print("Вода в чайнике вскипела")
                self.status = "off"



class Sensor(Device):
    def __int__(self, room="Hall", temperature=23, humidity=30, status="on"):
        super().__init__(status)
        self.temperature = 23
        self.humidity = humidity
        self.room = room

    def get_inf(self):
        if self.status == "on":
            print("Текущая темпрература" + str(self.temperature))
            print("Текущая влажность" + str(self.humidity))


if __name__ == "__main__":
    teapot = Teapot()
    print(teapot.status)
    input("Нажмите enter чтобы включить чайник\n")
    teapot.switch()
    tc = multiprocessing.Process(target=teapot.boil_water, args=())
    tc.start()
    print(teapot.status)
    input("Нажмите enter чтобы увидеть температуру воды\n")
    teapot.get_inf()

