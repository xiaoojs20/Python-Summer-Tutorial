# 2-1
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = [ele + 1 for ele in a]
# print(a)

# 2-2
# li=[i**i for i in range(1,10)]
# print(li)

# 2-3
# even=[i for i in range(1,11) if i%2==0]
# print(even)

# 2-4
# even2=[i**2 for i in [j for j in range(1,11) if j%2==0]]
# print(even2)

# 2-5
# li=["Abc",123,'tesT',666]
# a=[i.lower() for i in li if isinstance(i,str)]
# print(a)

# 2-6
# a=[f'{i}*{j}={i*j}' for i in range(1,10) for j in range(1,10) if i<=j]
# print(a)

# 2-7
# li=[i for i in range(2,100) if 0 not in [i % d for d in range(2, i)]]
# print(li)
