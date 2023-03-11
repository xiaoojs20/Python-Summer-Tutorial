import random


class Animal:
    def __init__(self, id, name, life, power, weight, pos):
        self.id = id
        self.name = name
        self.life = life
        self.power = power
        self.weight = weight
        self.pos = pos

    def move(self, pos):
        self.pos[0] += pos[0]
        self.pos[1] += pos[1]
        print(f'{self.name}移动{pos}到{self.pos}')


class Human(Animal):
    def __init__(self, id, name, life, power, weight, pos, father, mother):
        super().__init__(id, name, life, power, weight, pos)
        self.father = father
        self.mother = mother

    def move(self, pos):
        super().move(pos)

    def shout(self, info):
        print(f'{self.name},life:{self.life},power:{self.power},weight:{self.weight},pos:{self.pos},'
              f'father:{self.father0},mother:{self.mother}')
        print(info)

    def attack(self, dog):
        dog.life -= random.randint(1, self.power)
        print(f'{self.name} attack {dog.name} remain life {dog.life}')


class Dog(Animal):
    def __init__(self, id, name, life, power, weight, pos, price):
        super().__init__(id, name, life, power, weight, pos)
        self.price = price

    def move(self, pos):
        super().move(pos)

    def bark(self, info):
        print(f'{self.name},life:{self.life},power:{self.power},weight:{self.weight},pos:{self.pos},price:{self.price}')
        print(info)

    def bite(self, human):
        human.life -= random.randint(1, self.power)
        print(f'{self.name} bite {human.name} remain life {human.life}')


h0 = Human("000", "王零", 100, 10, 60, [0, 0], "王", "零")
h1 = Human("001", "王一", 100, 10, 60, [0, 1], "王", "一")
h2 = Human("002", "王二", 100, 10, 60, [0, 2], "王", "二")
h3 = Human("003", "王三", 100, 10, 60, [0, 3], "王", "三")
h4 = Human("004", "王四", 100, 10, 60, [0, 4], "王", "四")
h5 = Human("005", "王五", 100, 10, 60, [1, 0], "王", "五")
h6 = Human("006", "王六", 100, 10, 60, [1, 1], "王", "六")
h7 = Human("007", "王七", 100, 10, 60, [1, 2], "王", "七")
h8 = Human("008", "王八", 100, 10, 60, [1, 3], "王", "八")
h9 = Human("009", "王九", 100, 10, 60, [1, 4], "王", "九")

d0 = Dog("000", "狗零", 100, 10, 60, [3, 0], 0)
d1 = Dog("001", "狗一", 100, 10, 60, [3, 1], 1)
d2 = Dog("002", "狗二", 100, 10, 60, [3, 2], 2)
d3 = Dog("003", "狗三", 100, 10, 60, [3, 3], 3)
d4 = Dog("004", "狗四", 100, 10, 60, [3, 4], 4)
d5 = Dog("005", "狗五", 100, 10, 60, [4, 0], 5)
d6 = Dog("006", "狗六", 100, 10, 60, [4, 1], 6)
d7 = Dog("007", "狗七", 100, 10, 60, [4, 2], 7)
d8 = Dog("008", "狗八", 100, 10, 60, [4, 3], 8)
d9 = Dog("009", "狗九", 100, 10, 60, [4, 4], 9)

h_list = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9]
d_list = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]

while True:
    new_h = []
    new_d = []
    # 在10*10的二维矩阵上随机移动
    for i in range(len(h_list)):
        x = random.randint(0 - h_list[i].pos[0], 4 - h_list[i].pos[0])
        y = random.randint(0 - h_list[i].pos[1], 4 - h_list[i].pos[1])
        pos = [x, y]
        if h_list[i].pos != [-1, -1]:
            h_list[i].move(pos)

        for j in range(len(d_list)):
            if h_list[i].pos == d_list[j].pos and h_list[i].pos != [-1,-1]:
                print(f'{h_list[i].name}和{d_list[j].name}相遇')
                h_list[i].attack(d_list[j])
                d_list[j].bite(h_list[i])

                if d_list[j].life <= 0:
                    d_list[j].pos = [-1,-1] # 死亡区
                    print(f"{d_list[j].name} is dead")
                if h_list[i].life <= 0:
                    h_list[i].pos = [-1,-1] # 死亡区
                    print(f"{h_list[i].name} is dead")
            else:
                continue

    for i in range(len(d_list)):
        x = random.randint(0 - d_list[i].pos[0], 4 - d_list[i].pos[0])
        y = random.randint(0 - d_list[i].pos[1], 4 - d_list[i].pos[1])
        pos = [x, y]
        if d_list[i].pos != [-1,-1]:
            d_list[i].move(pos)

        for j in range(len(h_list)):
            if d_list[i].pos == h_list[j].pos and h_list[j].pos != [-1,-1] :
                print(f'{d_list[i].name}和{h_list[j].name}相遇')
                d_list[i].bite(h_list[j])
                h_list[j].attack(d_list[i])
                if h_list[j].life <= 0:
                    h_list[j].pos = [-1,-1] # 死亡区
                    print(f"{h_list[j].name} is dead")
                if d_list[i].life <= 0:
                    d_list[i].pos= [-1,-1] # 死亡区
                    print(f"{d_list[i].name} is dead")
            else:
                continue

    for idx in range(len(h_list)):
        if h_list[idx].life > 0:
            new_h.append(h_list[idx])
    for idx in range(len(d_list)):
        if d_list[idx].life > 0:
            new_d.append(d_list[idx])

    h_list = new_h
    d_list = new_d

    if len(new_h) == 0:
        print("Dogs win")
        break
    elif len(new_d) == 0:
        print("Human win")
        break


