# 你现在是一家游戏公司的开发人员，现在需要你开发一款叫做<人狗大战>的游戏：
# 至少需要2个角色，一个是人， 一个是狗。
# 不同的角色有不同的属性。
# 人和狗都有不同的技能，比如人拿棍打狗， 狗可以咬人。
# 怎么描述这种不同的角色和他们的功能呢？

import random


class Person():
    def __init__(self, name, life_value, attack_value):
        self.name = name
        self.life_value = life_value
        self.attack_value = attack_value

    def talk(self):
        print("Hello, my name is %s, My life value is %s and attack value is %s!"
              % (self.name, self.life_value, self.attack_value))

    def attack(self, dog):
        dog.life_value -= random.randint(0,self.attack_value)
        print("Person %s attack Dog %s remain life: %s" % (self.name, dog.name, dog.life_value))


class Dog(object):
    def __init__(self, name, life_value, attack_value):
        self.name = name
        self.life_value = life_value
        self.attack_value = attack_value

    def bite(self, person):
        person.life_value -= random.randint(0,self.attack_value)
        print("Dog %s bite Person %s remain life: %s" % (self.name, person.name, person.life_value))


p1 = Person("amao", 1000, 4)
print(p1.name, p1.life_value, p1.attack_value)
d1 = Dog("agou", 100, 10)
print(d1.name, d1.life_value, d1.attack_value)
p1.attack(d1)
d1.bite(p1)

while True:
    p1.attack(d1)
    d1.bite(p1)
    if p1.life_value <= 0:
        print(f'{p1.name} is dead')
        break
    elif d1.life_value <= 0:
        print(f'{d1.name} is dead')
        break
