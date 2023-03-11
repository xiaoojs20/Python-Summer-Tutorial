class Shape:
    def __init__(self):
        pass


class Rect:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def perimeter(self):
        print(f'长方形周长为{2 * (self.x + self.y)}')

    def area(self):
        print(f'长方形面积为{self.x * self.y}')


class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        print(f'圆形周长为{3.14 * 2 * self.r}')

    def area(self):
        print(f'圆形面积为{3.14 * self.r * self.r}')


class Square:
    def __init__(self, a):
        self.a = a

    def perimeter(self):
        print(f'正方形周长为{4 * self.a}')

    def area(self):
        print(f'正方形面积为{self.a * self.a}')


def get_shape(name, *args, **kwargs):
    name = name.capitalize()
    cls = globals().get(name, None)
    if cls:
        return cls(*args, **kwargs)
    else:
        return Shape(*args, **kwargs)

    # if name == "rect":
    #     return Rect(*args, **kwargs)
    # elif name == "circle":
    #     return Circle(*args, **kwargs)
    # elif name == "square":
    #     return Square(*args, **kwargs)
    # return Shape(*args, **kwargs)


# 静态生成
r1 = Rect(5, 6)
r1.perimeter()
r1.area()

c1 = Circle(3)
c1.perimeter()
c1.area()

s1 = Square(4)
s1.perimeter()
s1.area()

# 动态生成
x1 = get_shape("rect", 3, 4)
x1.perimeter()
x1.area()
