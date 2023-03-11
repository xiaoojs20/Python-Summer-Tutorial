# 7.	编写程序，定义1个人类（Person），要求：
# 	包含id、name、power，3个属性。
# 	默认体力（power）100。
# 	吃饭（eat）恢复体力20，睡觉（sleep）恢复体力50，学习（study）消耗体力30，练习（training）消耗体力25。

class Person:
    def __init__(self, id, name, power = 100):
        self.id = id
        self.name = name
        self.power = power
        print(f'{self.name}的体力为{self.power}')

    def eat(self):
        self.power += 20
        print(f'{self.name}吃饭，体力变为{self.power}')

    def sleep(self):
        self.power += 50
        print(f'{self.name}睡觉，体力变为{self.power}')

    def study(self):
        self.power -= 30
        print(f'{self.name}学习，体力变为{self.power}')

    def training(self):
        self.power -= 25
        print(f'{self.name}练习，体力变为{self.power}')

p1 = Person("0001","亚当")
p1.eat()
p1.study()
p1.sleep()
p1.training()