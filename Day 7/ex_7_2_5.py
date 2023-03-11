class Person:
    def __init__(self, id, name, age, weight):
        self.id = id
        self.name = name
        self.age = age
        self.weight = weight

    def run(self):
        print(f"{self.name} is running")

    def say(self):
        print(f'{self.name} is saying')

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def __delitem__(self, key):
        del self.__dict__[key]


p1 = Person("001", "小明", 18, 65)
print(p1["id"], p1["name"], p1["age"], p1["weight"])
