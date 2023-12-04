"""Модули для ввода и вывода значений"""
from my_module import Input


class SmartHouse:
    __devices = []
    __numbers = {}

    @classmethod
    def new_device(cls, type, room):
        if type == 1:
            cls.__devices.append(LightBulb(room, SmartHouse.check_number(type, room)))
        elif type == 2:
            cls.__devices.append(Teapot(room, SmartHouse.check_number(type, room)))
        elif type == 3:
            cls.__devices.append(Sensor(room, SmartHouse.check_number(type, room)))
        elif type == 4:
            cls.__devices.append(RobotVacumCleaner(room, SmartHouse.check_number(type, room)))
        elif type == 5:
            cls.__devices.append(StereoSpeaker(room, SmartHouse.check_number(type, room)))

    @classmethod
    def devices(cls):
        return cls.__devices

    @classmethod
    def check_number(cls, type, room):
        type = str(type)
        try:
            cls.__numbers[type + room] += 1
        except KeyError:
            cls.__numbers[type + room] = 1
        return cls.__numbers[type + room]


class Device:
    """Класс всех устройств"""
    def __init__(self, name, room, number, status="выключен(а)",):
        self.status = status
        self.name = name
        self.room = room
        self.number = number

    def switch(self):
        """Функция меняющая статус устройства"""
        if self.status == "выключен(а)":
            self.status = "включен(а)"
            return "Устройство включено"
        else:
            self.status = "выключен(а)"
            return "Устройство выключено"

    def get_status(self):
        """Функция пишуща статус устройства"""
        return (self.name + " находящийся в комнате "
              + self.room + " сейчас" + self.status)

    @staticmethod
    def get_functions():
        """Функция пишущая функции устройства"""
        return("1) Узнать статус устройства"
               "\n2) Включить или выключить устройство")


class LightBulb(Device):
    """Класс лампочек"""
    def __init__(self, room, number):
        super().__init__("Лампочка", room, number)


class Teapot(Device):
    """Класс чайников"""
    def __init__(self, room, number, ):
        super().__init__("Чайник", room, number)
        self.temperature = 23.0

    def get_inf(self):
        """Фукция пишущая текущую температуру воды в чайнике"""
        return "Температура воды в чайнике: " + str(self.temperature)

    def switch(self):
        """Фунция включающая чайник"""
        self.status = "включен(а)"
        self.temperature = 100
        self.status = 'выключен(а)'
        return "Вода в чайнике вскипела. Чайник выключен"

    def function(self):
        """Функция вызывающая дополнительную функцию устройства"""
        self.get_inf()

    def get_functions(self):
        """Функция пишущая функции устройства"""
        return super().get_functions() + "\n3) Узнать температуру воды в чайнике"


class StereoSpeaker(Device):
    """Класс музыкальных колонок"""
    def __init__(self, room, number):
        super().__init__("Музыкальная колонка", room, number)
        self.volume = 5

    def turn_up_the_volume(self):
        if self.volume < 10:
            self.volume += 1
            return "Текущая громкость: ", self.volume
        else:
            return "Громкость максимальная (10)"

    def turn_down_the_volume(self):
        if self.volume > 0:
            self.volume -= 1
            return "Текущая громкость: ", self.volume
        else:
            return "Текущая громкость минимальная (0)"

    def get_functions(self):
        """Функция пишущая функции устройства"""
        super().get_functions()
        print("3) Изменить громкость")


class Sensor(Device):
    """Класс сенсоров"""
    def __init__(self, room, number, temperature=23, humidity=30):
        super().__init__("Сенсор", room, number, "включен(а)")
        self.temperature = temperature
        self.humidity = humidity
        self.room = room

    def get_inf(self):
        """Функция возвращающая текущую температуру и влажность"""
        if self.status == "on":
            print("Текущая темпрература" + str(self.temperature))
            print("Текущая влажность" + str(self.humidity))
        else:
            print("В начале необходимо включить устройство")

    def function(self):
        """Функция вызывающая дополнительную функцию устройства"""
        self.get_inf()

    def get_functions(self):
        """Функция пишущая функции устройства"""
        return super().get_functions() + "\n3) Получить информацию с датчика"


class RobotVacumCleaner(Device):
    """Класс роботов пылесосов"""
    def __init__(self, room, number):
        super().__init__("Робот пылесос", room, number)

    def switch(self):
        """Функция меняющая статус устройства"""
        self.status = "on"
        print("Квартира убранна")
        self.status = "off"


class Terminal:
    """Клас терминала для связи с пользователем"""
    @staticmethod
    def menu():
        """Функция вызывающая меню"""
        print("Здравствуте, вы находитесь в системе умный дом.")
        while True:
            print("Выберите действие, которое вы хотите совершить:"
                  "\n1)Перейти к управлению устройствами"
                  "\n2)Добавить новое устройство в систему")
            command = Input.command(2)
            if command == 1:
                Terminal.device_management()
            if command == 2:
                Terminal.append_new_device()


    @staticmethod
    def append_new_device():
        while True:
            print("Выберите тип устройства"
                  "\n1)Лампочка"
                  "\n2)Чайник"
                  "\n3)Сенсор"
                  "\n4)Робот пылесос"
                  "\n5)Музыкалькая колонка")
            command = Input.command(5)
            if not command:
                break
            print("Введите название комнаты, в которой находится устройство")
            room = Input.str()
            if not room:
                continue
            SmartHouse.new_device(command, room)
            print("Нововое устройство успеншо добавлено")
            break

    @staticmethod
    def device_management():
        while True:
            print("Выберите доступное устройство")
            for device in range(len(SmartHouse.devices())):
                print(str(device+1) + ") " + SmartHouse.devices()[device].name + " ("
                      + SmartHouse.devices()[device].room
                      + ") (" + str(SmartHouse.devices()[device].number) + ")")
            command = Input.command(len(SmartHouse.devices()))
            if not command:
                break
            device = command - 1
            while True:
                print("Выберете действие которое хотите совершить:")
                print(SmartHouse.devices()[device].get_functions())
                command = Input.command(3)
                if not command:
                    break
                if command == 1:
                    print(SmartHouse.devices()[device].switch)
                elif command == 2:
                    print(SmartHouse.devices()[device].get_status)
                elif "function" in dir(SmartHouse.devices()[device]):
                    print(SmartHouse.devices()[device].function)
                else:
                    print("Комманда введена не верно")


if __name__ == "__main__":
    SmartHouse.new_device(1, "Зал")
    SmartHouse.new_device(1, "Зал")
    Terminal.menu()
    print(SmartHouse.devices())