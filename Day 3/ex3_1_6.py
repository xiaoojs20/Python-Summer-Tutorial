i = 1
a = []
b = []
try:
    while True:
        j = i + 1
        i += 1
        # a = int('aaa')
        if i >= 10:
            break
        raise ValueError("haaha")
except NameError as e:
    print(e)
except IndentationError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print("没有异常！")
finally:
    print("有没有异常都会执行到我！")

print(i)

