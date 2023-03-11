# 网站要求用户输入用户名和密码进行注册。编写程序以检查用户输入的密码的有效性，输出密码是否符合要求，若不符合要求，还应同时输出为何不符合要求。以下是检查密码的标准：
# 至少有一个小写字母
# 至少有一个数字
# 至少有一个大写字母
# 至少有一个“@、#、$、%、&”字符
# 密码的最小长度：6
# 密码的最大长度：12

li=['@','#','$','%','&']
wrong=0
password=input("please set your password")
upper=0
lower=0
number=0
other=0

for i in range(len(password)):
    if password[i].isupper():
        upper+=1
    elif password[i].islower():
        lower+=1
    elif password[i].isdigit():
        number+=1
    elif password[i] in li:
        other+=1

if lower==0:
    print("密码不符合要求，至少有一个小写字母")
    wrong=1
if upper==0:
    print("密码不符合要求，至少有一个大写字母")
    wrong=1
if number==0:
    print("密码不符合要求，至少有一个数字")
    wrong=1
if other==0:
    print("密码不符合要求，至少有一个“@、#、$、%、&”字符")
    wrong=1
if len(password)<6:
    print("密码不符合要求，密码的最小长度：6")
    wrong=1
if len(password)>12:
    print("密码不符合要求，密码的最大长度：12")
    wrong=1

if(wrong==0):
    print("密码设置成功")