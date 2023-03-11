# 6.编写程序，创建一个管理产品库存的应用。
# 	建立一个产品类:价格、id、库存数量。
# 	建立一个库存类:记录各种产品并能计算库存的总价值。

class Product:
    def __init__(self, price, name, id, number):
        self.price = price
        self.name = name
        self.id = id
        self.number = number


class Warehouse:
    list = []

    def __init__(self):
        print("建立新仓库")

    def add_product(self,product):
        for idx in range(len(Warehouse.list)):
            if product.name == Warehouse.list[idx]:
                Warehouse.list[idx] = [product.price, product.name, product.id, product.number]
                print("补货成功")
                break
        else:
            tmp = [product.price, product.name, product.id, product.number]
            print("进货成功")
            Warehouse.list.append(tmp)

    def del_product(self,product):
        for idx in range(len(Warehouse.list)):
            if product.name == Warehouse.list[idx][1]:
                if product.number <= Warehouse.list[idx][3]:
                    print("取出成功")
                    Warehouse.list[idx][3] -= product.number
                    break
                else:
                    print("仓库里该产品数量不足")
                    break
        else:
            print("仓库里没有该产品")
    def find_product(self, arg):
        pass

    def total_price(self):
        self.sum = 0
        for idx in range(len(Warehouse.list)):
            print(f'{Warehouse.list[idx][1]}:{Warehouse.list[idx][3]}件')
            self.sum += Warehouse.list[idx][0]*Warehouse.list[idx][3]
        print(f"总价值为{self.sum}")

p1 = Product(3,"乌龙茶","0001",500)
p2 = Product(50,"保温杯","0020",60)
w1 = Warehouse()
w1.add_product(p1)
w1.total_price()
w1.add_product(p2)
w1.total_price()
w1.del_product(p1)
w1.total_price()
