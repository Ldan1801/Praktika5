from my_module import Input, Print


class Device:
    def __init__(self, name, room, status="выключен(а)"):
        list_of_device[len(list_of_device)+1] = name
        my_device.append(self)
        self.status = status
        self.name = name
        self.room = room

    def switch(self):
        if self.status == "выключен(а)":
            print("Устройство включено")
            self.status = "включен(а)"
        else:
            print("Устройство выключено")
            self.status = "выключен(а)"
    
    def get_status(self):
        print(self.name + " находящийся в комнате " + self.room + " сейчас" + self.status)
    
    @staticmethod
    def get_functions():
        print("1) Узнать статус устройства\n"
              "2) Включить или выключить устройство")


class LightBulb(Device):

    def __init__(self, room, number=1,):
        super().__init__("Лампочка (" + room + str(number) + ")", room)
        self.room = room
        self.number = number


class Teapot(Device):
    def __init__(self, temperature=23.0, room="Кухня"):
        super().__init__("Чайник", room)
        self.temperature = temperature

    def get_inf(self):
        print("Температура воды в чайнике: " + str(self.temperature))

    def switch(self):
        print("Чайник включён")
        self.status = "включен(а)"
        self.temperature = 100
        self.status = 'выключен(а)'
        print("Вода в чайнике вскипела. Чайник выключен")

    def function(self):
        self.get_inf()

    def get_functions(self):
        super().get_functions()
        print("3) Узнать температуру воды в чайнике")


class StereoSpeaker(Device):
    def __init__(self, volume=5, room="Зал"):
        super().__init__("Музыкальная колонка", room)
        self.volume = volume

    def change_volume(self,):
        print('Нажмите "1", чтобы уменьшить громкость, или "2", чтобы увеличть громкость')
        flag = Input.command(2)
        while flag:
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
            flag = Input.command(2)

    def function(self):
        self.change_volume()

    def get_functions(self):
        super().get_functions()
        print("3) Изменить громкость")


class Sensor(Device):
    def __init__(self, room="Зал", temperature=23, humidity=30):
        super().__init__("Сенсор", room, "включен(а)")
        self.temperature = temperature
        self.humidity = humidity
        self.room = room

    def get_inf(self):
        if self.status == "on":
            print("Текущая темпрература" + str(self.temperature))
            print("Текущая влажность" + str(self.humidity))
        else:
            print("В начале необходимо включить устройство")

    def function(self):
        self.get_inf()

    def get_functions(self):
        super().get_functions()
        print("3) Получить информацию с датчика")


class RobotVacumCleaner(Device):
    def __init__(self, room="Спальая"):
        super().__init__("Робот пылесос", room)

    def switch(self):
        self.status = "on"
        print("Квартира убранна")
        self.status = "off"


class Terminal:
    @staticmethod
    def menu():
        print("Здравствуте, вы находитесь в системе умный дом.")
        while True:
            print("Выберите доступное устройство")
            Print.dictionary(list_of_device)
            device = Input.command(len(list_of_device))
            if not device:
                print("Комманда введена не верно. Повторите попытку")
                continue
            print("Выберете действие")
            my_device[device-1].get_functions()
            if my_device[device - 1].name in ["Чайник", "Сенсор", "Музыкальная колонка"]:
                command = Input.command(3)
            else:
                command = Input.command(2)
            while command:
                if command == 1:
                    my_device[device-1].get_status()
                elif command == 2:
                    my_device[device-1].switch()
                else:
                    my_device[device - 1].function()
                print("Выберете действие")
                my_device[device - 1].get_functions()
                if my_device[device-1].name in ["Чайник", "Сенсор", "Музыкальная колонка"]:
                    command = Input.command(3)
                else:
                    command = Input.command(2)


if __name__ == "__main__":
    list_of_device = {}
    my_device = []
    light1 = LightBulb("зал", 1)
    light2 = LightBulb("зал", 2)
    light3 = LightBulb("спальная", 1)
    light4 = LightBulb("кухня", 1)
    teapot = Teapot()
    sensor = Sensor()
    robot_vacuum_cleaner = RobotVacumCleaner()
    stereo_speaker = StereoSpeaker()
    Terminal.menu()
