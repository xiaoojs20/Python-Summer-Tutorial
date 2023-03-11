class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def run(self):
        print(f"{self.name} is running")

    def say(self):
        print(f'{self.name} is saying')


def swim(p):
    print(f"{p.name} is swimming")


def playgame(p):
    print(f"{p.name} is playing games")


p1 = Person("001", "小明", 18)
p1.run()
p1.say()

p2 = Person("002", "小红", 16)

setattr(p2,"country","中国")
setattr(p2,"school","清华大学")
print(p2.country)


setattr(p2,"swim",swim)
p2.__setattr__("playgame",playgame)

p2.swim(p2)
p2.playgame(p2)

print(hasattr(p2, "school"))
print(hasattr(p2, "playgame"))

delattr(p2, "school")
p2.__delattr__("playgame")

print(getattr(p2, "school",None))
print(hasattr(p2, "playgame"))

print(p1.__dict__)
print(p2.__dict__)
