class Phone():
    def __init__(self, number):
        self._number = number

    def call(self, number):
        if self._number == number:
            raise ValueError("不能呼叫自己的号码")
        self.__phone_to_base_station(self._number)
        self.__base_station_call_phone(number)
        self.__phone_to_phone(Phone(number))

    def __phone_to_base_station(self, my_number):
        print(f"{my_number}与基站通信")

    def __base_station_call_phone(self, her_number):
        print(f"基站与{her_number}通信")

    def __phone_to_phone(self, phone):
        print(f"{self._number}与{phone._number}建立链接")


p1 = Phone("0001")
p1.call("0002")
p2 = Phone("0002")
p2.call("0001")
p2.call("0002")
