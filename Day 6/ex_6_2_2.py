# 两人PK
# 1、需要有昵称，攻击力，生命值等属性。
# 2、实例化两个人物。
# 3、人物之间互相殴打，若某一方的生命值 <=0，则判定为死亡，战斗结束。

import random


class ADC():
    def __init__(self, name, life_value, attack_value):
        self.name = name
        self.life_value = life_value
        self.attack_value = attack_value

    def attack(self, enemy):
        enemy.life_value -= random.randint(0, self.attack_value)
        print("ADC %s 攻击 Tank %s 剩余血量 : %s" % (self.name, enemy.name, enemy.life_value))


class Tank(object):
    def __init__(self, name, life_value, attack_value):
        self.name = name
        self.life_value = life_value
        self.attack_value = attack_value

    def bite(self, person):
        person.life_value -= random.randint(0, self.attack_value)
        print("Tank %s 攻击 ADC %s 剩余血量: %s" % (self.name, person.name, person.life_value))


p0 = ADC("鲁班", 500, 37)
p1 = ADC("伽罗", 600, 38)
p2 = ADC("后羿", 700, 35)
p3 = ADC("成吉思汗", 500, 36)
p4 = ADC("黄忠", 800, 28)
p5 = ADC("狄仁杰", 600, 30)
p6 = ADC("蒙犽", 800, 28)
p7 = ADC("孙尚香", 600, 32)
p8 = ADC("艾琳", 600, 25)
p9 = ADC("李元芳", 700, 30)
p_list = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9]
d0 = Tank("程咬金", 1500, 12)
d1 = Tank("典韦", 900, 19)
d2 = Tank("廉颇", 1400, 17)
d3 = Tank("亚瑟", 1400, 15)
d4 = Tank("凯", 800, 22)
d5 = Tank("项羽", 1600, 12)
d6 = Tank("孙策", 1100, 20)
d7 = Tank("钟无艳", 1000, 18)
d8 = Tank("夏侯惇", 1400, 15)
d9 = Tank("蒙恬", 1500, 17)
d_list = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]

while True:
    p_list[random.randint(0, len(p_list)-1)].attack(d_list[random.randint(0, len(d_list)-1)])
    d_list[random.randint(0, len(d_list)-1)].bite(p_list[random.randint(0, len(p_list)-1)])
    # 死亡后删除
    new_p = []
    new_d = []
    for idx in range(len(p_list)):
        if p_list[idx].life_value <= 0:
            print(f'{p_list[idx].name} 死亡')
        elif p_list[idx].life_value > 0:
            new_p.append(p_list[idx])

    for idx in range(len(d_list)):
        if d_list[idx].life_value <= 0:
            print(f'{d_list[idx].name} 死亡')
        elif d_list[idx].life_value > 0:
            new_d.append(d_list[idx])

    if len(new_p) == 0:
        print("Tank 胜利")
        break
    if len(new_d) == 0:
        print("ADC 胜利")
        break
    p_list = new_p
    d_list = new_d


