class Animal:
    def __init__(self,sex,power):
        self.sex = sex
        self.power = power

    def get_power(self):
        print(f'power:{self.power}')


class Cat(Animal):
    def __init__(self,name,sex,power):
        super().__init__(sex,power)
        self.name = name

class Dog(Animal):
    def __init__(self, name,sex, power):
        super().__init__(sex, power)
        self.name = name

class Human(Animal):
    def __init__(self,name,sex):
        self.name = name

    def feed(self,animal):
        print(f'feed {animal.name}')
        animal.power += 10

c1 = Cat("miao","female",50)
c1.get_power()
d1 = Dog("wang","male",80)
d1.get_power()
h1 = Human("xiaoming","male")
h1.feed(c1)
c1.get_power()
d1.get_power()