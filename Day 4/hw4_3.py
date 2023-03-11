# 写一个用户注册和登录验证程序，文件名account.json，内容如下
import os, json,time, hashlib
# dic = {"account":"name", "expire_date": "2021-01-01", "status": 0, "password": "abc"}
dic = {}
register_or_login = input("注册按1,登录按2")

# a)用户注册：
if register_or_login == '1':
    print("现在开始注册")
    # i.输入用户名称（需要检查用户名称是否已经被注册）
    while True:
        name = input("请输入用户名称")
        file_name = name + '.json'

        if not os.path.exists(file_name):
            print("用户名尚未注册")
            break
        else:
            print("用户名已经被注册,请重新输入用户名")
            continue

    # ii.两次输入用户密码（用户密码需要至少6位，至少包含数字字母和下划线），检查两次输入的用户密码是否不一致。
    while True:
        password1 = input("请设置用户的密码")
        if len(password1) < 6:
            print("密码设置至少需要6位")
            continue
        is_legal = [False, False, False]
        for i in range(len(password1)):
            if password1[i].isdigit():
                is_legal[0] = True
            elif password1[i].isalpha():
                is_legal[1] = True
            elif password1[i] == '_':
                is_legal[2] = True
            else:
                break
        if False in is_legal:
            print("密码至少包含数字字母和下划线")
            continue
        password2 = input("请再次输入密码")
        if password1 != password2:
            print("两次输入的密码不同,请重新设置密码")
            continue
        else:
            print("密码设置成功")
            break
    # iii.输入用户有效期。
    period = input("请输入用户有效期(单位:天)")
    t0 = time.time()
    t1 = t0 + int(period)*24*3600
    expire_date = time.strftime("%Y-%m-%d", time.localtime(t1))
    print(expire_date)

    # iv.结果保存到 account.json，account 是 用户名称。
    # iv.不要明文存储密码，要采用 hash来加密
    # dic = {"expire_date": "2021-01-01", "status": 0, "password": "abc"}
    m1 = hashlib.md5()
    m1.update(password1.encode('utf-8'))
    encrypted_password = str(m1.digest())
    dic = {"expire_date": expire_date, "status": 0, "password": encrypted_password}
    print(dic)
    file_name = name + '.json'
    with open(file_name, 'w') as fp:
        json.dump(dic, fp)

# b)用户登录：
if register_or_login == '1' or register_or_login == '2':
    print("现在开始登录")
    # i.根据用户输入的用户名&密码，找到对应的json文件，把数据加载出来进行验证
    # dic = {"expire_date": "2021-01-01", "status": 0, "password": "abc"}
    # ii.用户名为json文件名，密码为 password所对应的值。
    times = 0
    while True:
        name = input("请输入用户名")
        file_name = name + '.json'
        if not os.path.exists(file_name):
            print("用户名尚未注册,请重新输入用户名")
            continue
        else:
            with open(file_name) as f:
                dic = json.load(f)
                print(dic)
        # iii.判断账号是否过期或者被锁定
        if dic["status"] == '1':
            print("你的账号已经锁定")
        local_time = time.strptime(dic["expire_date"], '%Y-%m-%d')
        t_time = time.mktime(local_time)
        if t_time < time.time():
            print("你的账号已经过期")

        password = input("请输入密码")
        m2 = hashlib.md5()
        m2.update(password.encode('utf-8'))
        password = str(m2.digest())
        if password == dic["password"]:
            print("密码正确,登陆成功")
            break
        else:
            print("密码错误,登录失败")
            times += 1
            # v.登陆成功后，打印“登陆成功”，三次登陆失败，status值改为1，并且锁定账号。
            if times == 3:
                print("三次登录失败,账号已被锁定")
                dic["status"] == 1
                break
            else:
                continue
else:
    print("输入错误,请重新运行")
    exit()
