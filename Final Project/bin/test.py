while True:
    x = int(input("start"))
    y = int(input("end"))
    for num in range(x,y):
        if num%6 !=0:
            print(num,end=" ")
    print("")