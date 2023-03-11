# 编写一个接受句子的程序，并计算大写字母和小写字母的数量。
# 假设为程序提供了以下输入：
# Hello world!
# 输出：
# 大写字母 1个
# 小写字母 9个

upper=0
lower=0
sentence=input("please input a sentence")
for i in range(len(sentence)):
    if sentence[i].isupper():
        upper+=1
    elif sentence[i].islower():
        lower+=1
print(f'大写字母 {upper}个')
print(f'小写字母 {lower}个')

