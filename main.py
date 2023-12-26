"""Module for input and output of values"""
from my_module import Input


class SmartHouse:
    """
    Class for device menegment

    Attribtes
    ---------
    :param __devices:list
        list of the devices
    :param __nembers:dictionary
        a dictionary that stores a number of devices of the same type
    """
    __devices = []
    __numbers = {}

    @classmethod
    def new_device(cls, kind, room):
        """
        creates a new devic and append it in list __devices

        Parameters
        ----------
        :param kind:int
            an integer that defines the type of device
        :param room:str
            the room where the device is located

        :return:None
        """
        if kind == 1:
            cls.__devices.append(LightBulb
                                 (room, SmartHouse.check_number(kind, room)))
        elif kind == 2:
            cls.__devices.append(Teapot
                                 (room, SmartHouse.check_number(kind, room)))
        elif kind == 3:
            cls.__devices.append(Sensor
                                 (room, SmartHouse.check_number(kind, room)))
        elif kind == 4:
            cls.__devices.append(RobotVacumCleaner
                                 (room, SmartHouse.check_number(kind, room)))
        elif kind == 5:
            cls.__devices.append(StereoSpeaker
                                 (room, SmartHouse.check_number(kind, room)))

    @classmethod
    def devices(cls):
        """
        return list if devices

        :return: __devices
        """
        return cls.__devices

    @classmethod
    def check_number(cls, kind, room):
        """
        checks the number of devices of this kind in one room

        Parameters
        ----------
        :param kind:int
            an integer that defines the type of device
        :param room:
            the room where the device is located

        :return: __numbers: dectionary
        """
        kind = str(kind)
        try:
            cls.__numbers[kind + room] += 1
        except KeyError:
            cls.__numbers[kind + room] = 1
        return cls.__numbers[kind + room]

    @classmethod
    def remove_device(cls, index):
        """
        delete device from list of devices

        Parameters
        ----------
        :param index: int
            index of device wich we wont delete

        :return:None
        """
        del cls.__devices[index]


class Device:
    """
    Class represents a smart house devices

    Attributes
    ----------
    :param name: str
        name of the device
    :param room: str
        the room where the device is located
    :param number: int
        the number of devices of this kind in one room
    :param status
        device status

    Methods
    -------
    switch(self):
        changes the status of the device
    get_status(self):
        get the status of the device
    get_functions(self):
        get the functions of the device
    """
    def __init__(self, name, room, number, status="выключен(а)",):
        """
        states all necessary attributes of class

        Parametrs
        ---------
        :param name:str
        :param room:str
        :param number:int
        :param status:str
        """
        self.status = status
        self.name = name
        self.room = room
        self.number = number

    def switch(self):
        """
        changes the status of the device

        Parameters
        ----------
        :return: current status message
        """
        if self.status == "выключен(а)":
            self.status = "включен(а)"
            return "Устройство включено"
        self.status = "выключен(а)"
        return "Устройство выключено"

    def get_status(self):
        """
        get the status of the device

        Parameters
        ----------
        :return: current status message
        """
        return (self.name + " находящийся в комнате "
                + self.room + " сейчас " + self.status)

    @staticmethod
    def get_functions():
        """
        get the functions of the device

        Parameters
        ----------
        :return: message about the device function
        """
        return("1) Узнать статус устройства"
               "\n2) Включить или выключить устройство")


class LightBulb(Device):
    """
    Class represents a ligt buld

    Attributes
    ----------
    :param name: str
        name of the device
    :param room: str
        the room where the device is located
    :param number: int
        the number of devices of this kind in one room
    :param status
        device status

    Methods
    -------
    switch(self):
        changes the status of the device
    get_status(self):
        get the status of the device
    get_functions(self):
        get the functions of the device
    """
    def __init__(self, room, number):
        """
        states all necessary attributes of class

        Parameters
        ----------
        :param room: str
            the room where the device is located
        :param number: int
            the number of devices of this kind in one room
        """
        super().__init__("Лампочка", room, number)


class Teapot(Device):
    """
    Class represents a teapot

    Attributes
    ----------
    :param name: str
        name of the device
    :param room: str
        the room where the device is located
    :param number: int
        the number of devices of this kind in one room
    :param status: str
        device status
    :param temperature: int
        the temperature of the water in the teapot

    Methods
    -------
    switch(self):
        changes the status of the device
    get_status(self):
        get the status of the device
    get_functions(self):
        get the functions of the device
    get_inf(sels):
        get current water temperature in teapot
    funcion(self):
        calls an additional function of the device
    """
    def __init__(self, room, number, ):
        """
        states all necessary attributes of class

        Parameters
        ----------
        :param room: str
            the room where the device is located
        :param number: int
            the number of devices of this kind in one room
        """
        super().__init__("Чайник", room, number)
        self.temperature = 23.0

    def get_inf(self):
        """
        get current water temperature in teapot

        :return: int
            current water temperature in teapot messeg
        """
        return "Температура воды в чайнике: " + str(self.temperature)

    def switch(self):
        """
        changes the status of the device
        :return: current status message
        """
        self.status = "включен(а)"
        self.temperature = 100
        self.status = 'выключен(а)'
        return "Вода в чайнике вскипела. Чайник выключен"

    def function(self):
        """
        calls an additional function of the device
        """
        return self.get_inf()

    @staticmethod
    def get_functions():
        """
        get the functions of the device

        Parameters
        ----------
        :return: the device function messeg
        """
        return (super(Teapot, Teapot).get_functions()
                + "\n3) Узнать температуру воды в чайнике")


class StereoSpeaker(Device):
    """
    Class represents a smart house devices

    Attributes
    ----------
    :param name: str
        name of the device
    :param room: str
        the room where the device is located
    :param number: int
        the number of devices of this kind in one room
    :param status: str
        device status
    :param volume: int
        the volume of the music speaker

    Methods
    -------
    switch(self):
        changes the status of the device
    get_status(self):
        get the status of the device
    get_functions(self):
        get the functions of the device
    turn_up_the_volume(self):
        turn up the volume of stereo speaker
    turn_down_the_volume(self):
        turn down the volume of stereo speaker
    """
    def __init__(self, room, number):
        """
        states all necessary attributes of class

        Parameters
        ----------
        :param room: str
            the room where the device is located
        :param number: int
            the number of devices of this kind in one room
        """
        super().__init__("Музыкальная колонка", room, number)
        self.volume = 5

    def turn_up_the_volume(self):
        """
        turn up the volume of stereo speaker
        :return: current volime messeg
        """
        if self.volume < 10:
            self.volume += 1
            return "Текущая громкость: ", self.volume
        return "Громкость максимальная (10)"

    def turn_down_the_volume(self):
        """
        turn down the volume of stereo speaker
        :return: current volime messeg
        """
        if self.volume > 0:
            self.volume -= 1
            return "Текущая громкость: ", self.volume
        return "Текущая громкость минимальная (0)"

    @staticmethod
    def get_functions():
        """
        get the functions of the device

        Parameters
        ----------
        :return: the device function messeg
        """
        return (super(StereoSpeaker, StereoSpeaker).get_functions()
                + "\n3) Изменить громкость")


class Sensor(Device):
    """
    Class represents a smart house devices

    Attributes
    ----------
    :param name: str
        name of the device
    :param room: str
        the room where the device is located
    :param number: int
        the number of devices of this kind in one room
    :param status: str
        device status
    :param __temperature: int
        the current air temperature in the room
    :param __humidity: int
         the current air humidity in the room

    Methods
    -------
    switch(self):
        changes the status of the device
    get_status(self):
        get the status of the device
    get_functions(self):
        get the functions of the device
    git_inf(self):
        get current air temperature and humidity in the room
    """
    def __init__(self, room, number, temperature=23, humidity=30):
        """
        states all necessary attributes of class

        Parameters
        ----------
        :param room:str
            the room where the device is located
        :param number: int
            the number of devices of this kind in one room
        :param temperature:int
            the current air temperature in the room
        :param humidity:int
            the current air humidity in the room
        """
        super().__init__("Сенсор", room, number, "включен(а)")
        self.__temperature = temperature
        self.__humidity = humidity
        self.room = room

    def get_inf(self):
        """Функция возвращающая текущую температуру и влажность"""
        if self.status == "включен(а)":
            return ("Текущая темпрература: " + str(self.__temperature)
                    + "\nТекущая влажность: " + str(self.__humidity))
        return "В начале необходимо включить устройство"

    def function(self):
        """
        calls an additional function of the device
        """
        return self.get_inf()

    @staticmethod
    def get_functions():
        """
        get the functions of the device

        Parameters
        ----------
        :return: message about the device function
        """
        return (super(Sensor, Sensor).get_functions()
                + "\n3) Получить информацию с датчика")

    @humidity.setter
    def humidity(self,humidity):
        """
        set self.humidity

        Parameters:
        ----------
        :param humidity: int
            the current air humidity in the room

        :return: None

        :raise ValueError:

        Examples:
            >>> self.humidity = 40

            >>> self.humidity = -1
            Traceback (most recent call last):
                ...
            ValueError ("Введена отрицательная влажность")

            >>> self.humidity = -100
            Traceback (most recent call last):
                ...
            ValueError ("Введена влажность больше 100")
        """
        if 0 <= humidity <= 100:
            self.__humidity = humidity
        elif 0 > humidity:
            raise ValueError ("Введена отрицательная влажность")
        else:
            raise ValueError ("Введена влажность больше 100")


class RobotVacumCleaner(Device):
    """
    Class represents a smart house devices

    Attributes
    ----------
    :param name: str
        name of the device
    :param room: str
        the room where the device is located
    :param number: int
        the number of devices of this kind in one room
    :param status: str
        device status

    Methods
    -------
    switch(self):
        changes the status of the device
    get_status(self):
        get the status of the device
    get_functions(self):
        get the functions of the device
    """
    def __init__(self, room, number):
        """
        states all necessary attributes of class

        Parameters
        ----------
        :param room: str
            the room where the device is located
        :param number: int
            the number of devices of this kind in one room
        """
        super().__init__("Робот пылесос", room, number)

    def switch(self):
        """
        changes the status of the device
        :return: current status message
        """
        self.status = "включен(а)"
        self.status = "выключена"
        return "Квартира убранна. Устройство выключено"


class Terminal:
    """
    Class represent a terminal for communicating with the user

    Methods
    -------
    menu():
        calls the main menu
    append_new_device():
        requests data from the user to create a new device
    delete_device():
        requests data from the user to delete device
    device_menegment():
        requests data from the user to manage devices
    """
    @staticmethod
    def menu():
        """calls the main menu"""
        print("Здравствуте, вы находитесь в системе умный дом.")
        while True:
            print("Выберите действие, которое вы хотите совершить:"
                  "\n1)Перейти к управлению устройствами"
                  "\n2)Добавить новое устройство в систему"
                  "\n3)Удалить устройство из системы")
            command = Input.command(3)
            if command == 1:
                Terminal.device_management()
            if command == 2:
                Terminal.append_new_device()
            if command == 3:
                Terminal.delete_device()

    @staticmethod
    def append_new_device():
        """requests data from the user to create a new device"""
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
    def delete_device():
        """requests data from the user to delete device"""
        while True:
            print("Выберите устройство, которое хотите удалить")
            for device in range(len(SmartHouse.devices())):
                print(str(device + 1) + ") "
                      + SmartHouse.devices()[device].name + " ("
                      + SmartHouse.devices()[device].room
                      + ") (" + str(SmartHouse.devices()[device].number) + ")")
            command = Input.command(len(SmartHouse.devices()))
            if not command:
                break
            SmartHouse.remove_device(command-1)

    @staticmethod
    def device_management():
        """requests data from the user to manage devices"""
        while True:
            print("Выберите доступное устройство")
            for device in range(len(SmartHouse.devices())):
                print(str(device+1) + ") "
                      + SmartHouse.devices()[device].name + " ("
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
                    print(SmartHouse.devices()[device].get_status())
                elif command == 2:
                    print(SmartHouse.devices()[device].switch())
                elif "function" in dir(SmartHouse.devices()[device]):
                    print(SmartHouse.devices()[device].function())
                else:
                    print("Комманда введена не верно")


if __name__ == "__main__":
    SmartHouse.new_device(1, "Зал")
    SmartHouse.new_device(1, "Зал")
    SmartHouse.new_device(2, "Кухня")
    SmartHouse.new_device(3, "Зал")
    SmartHouse.new_device(4, "Зал")
    Terminal.menu()
