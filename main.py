from my_module import Input


class Device:
    def __init__(self, name, room, status="выкл"):
        self.status = status
        self.name = name
        self.room = room

    def switch(self):
        if self.status == "выкл.":
            print("Устройство включено")
            self.status = "вкл"
        else:
            print("Устройство выключено")
            self.status = "выкл"


class LightBulb(Device):
    def __init__(self, room, number=1,):
        super().__init__("Лампочка", room)
        self.room = room
        self.number = number


class Teapot(Device):
    def __init__(self, temperature=23.0, room="Кухня"):
        super().__init__("Чайник", room)
        self.temperature = temperature

    def get_inf(self):
        print("Температура воды в чайнике = " + str(self.temperature))

    def switch(self):
        print("Чайник включён")
        self.status = "вкл"
        self.temperature = 100
        self.status = 'выкл'
        print("Вода в чайнике вскипела")


class StereoSpeaker(Device):
    def __init__(self, volume=5, room="Зал"):
        super().__init__("Музыкальная колонка", room)
        self.volume = volume

    def change_volume(self, flag):
        if flag == 2:
            if self.volume < 10:
                self.volume += 1
                print("Текущая громкость: ", self.volume)
            else:
                print("Громкость максимальная (10)")
        elif flag == 1:
            if self.volume > 0:
                self.volume -= 1
                print("Текущая громкость: ", self.volume)
            else:
                print("Текущая громкость минимальная (0)")


class Sensor(Device):
    def __init__(self, room="Зал", temperature=23, humidity=30):
        super().__init__("Сенсор", room, "Вкл")
        self.temperature = temperature
        self.humidity = humidity
        self.room = room

    def get_inf(self):
        if self.status == "on":
            print("Текущая темпрература" + str(self.temperature))
            print("Текущая влажность" + str(self.humidity))


class RobotVacuumCleaner(Device):
    def __init__(self, room="Спальая"):
        super().__init__("Робот пылесос", room)

    def switch(self):
        self.status = "on"
        print("Квартира убранна")
        self.status = "off"


class Terminal:

    @staticmethod
    def menu():
        print("Здравствуте, вы находитесь в системе умный дом."
              "Выберете устройсто из досупны:\n"
              "1)Лампочки\n"
              "2)Чайник\n"
              "3)Робот-пылесос\n"
              "4)Музыкальная колонка\n"
              "5)Датчик влажности и температуры")
        command = Input.command(5)




if __name__ == "__main__":
    teapot = Teapot()
    light1 = LightBulb("зал", 1)
    light2 = LightBulb("зал", 2)
    light3 = LightBulb("спальная", 1)
    light4 = LightBulb("кухня", 1)
    sensor = Sensor()
    robot_vacuum_cleaner = RobotVacuumCleaner()
    stereo_speaker = StereoSpeaker()
    num = Input.int()
    print(num)

