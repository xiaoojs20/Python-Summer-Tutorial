class Person:
    """
    这是人类
    """
    __slots__ = ["name", "age", "weight", "height", "country"]

    def __init__(self, name, age, weight, height, country):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.country = country

    def run(self):
        print(f"{self.name} is running")

    def say(self):
        print(f'{self.name} is saying')


p1 = Person("小明", 18, 65, 180, "中国")
print(p1.__doc__)

print(p1.__module__)
print(p1.__class__)
print(type(p1))
print(type(p1).__name__)
print(p1.run.__name__)
func = p1.run
print(func.__name__)