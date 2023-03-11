from types import MethodType


class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def run(self):
        print(f"{self.name} is running")

    def say(self):
        print(f'{self.name} is saying')


def swim(self):
    print(f"{self.name} is swimming")


def playgame(self):
    print(f"{self.name} is playing games")


p1 = Person("001", "小明", 18)
p1.run()
p1.say()

p2 = Person("002", "小红", 16)
p2.country = "中国"
p2.school = "清华大学"

p2.swim = MethodType(swim, p2)
p2.playgame = MethodType(playgame, p2)

p2.swim()
p2.playgame()

print(hasattr(p2, "school"))
print(hasattr(p2, "playgame"))

delattr(p2, "school")
delattr(p2, "playgame")

print(hasattr(p2, "school"))
print(hasattr(p2, "playgame"))
