# 3-1
class person:
    def __init__(self, name, weight=70):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print(f'{self.name}体重为{self.weight}公斤')

    def eat(self):
        self.weight += 1
        print(f'{self.name}体重为{self.weight}公斤')


xm = person("小明")
xm.run()
xm.eat()


# 3-2
class soldier:
    def __init__(self, name, hisgun):
        self.name = name
        self.gun = hisgun

    def shoot(self):
        self.gun.bullet_num -= 1
        print(f'{self.name}的{self.gun.name}里子弹还有{self.gun.bullet_num}颗')


class gun:
    def __init__(self, name, number):
        self.name = name
        self.bullet_num = number

    def fill(self, number):
        self.bullet_num += number
        print(f'{self.name}的{self.name}里子弹还有{self.bullet_num}颗')


g1 = gun("AK47", 50)
p1 = soldier("许三多", g1)

p1.shoot()
p1.shoot()
p1.shoot()
p1.shoot()
p1.shoot()
p1.gun.fill(5)


# 3-3
class House():
    def __init__(self, square, houseitem=[]):
        self.square = square
        self.houseitem = houseitem
        print(f"新房子没有家具,占地面积为{self.square}")

    def add_houseitem(self, item):
        self.houseitem.append(item.name)
        self.square -= item.square
        item_str = ""
        for idx in range(len(self.houseitem)):
            item_str += self.houseitem[idx]
            if idx != (len(self.houseitem) - 1):
                item_str += '、'

        print(f'房子有家具:{item_str}，剩余面积为{self.square}')


class HouseItem():
    def __init__(self, name, square):
        self.name = name
        self.square = square


big_house = House(200)
bed = HouseItem("床", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 3.5)

big_house.add_houseitem(bed)
big_house.add_houseitem(chest)
big_house.add_houseitem(table)