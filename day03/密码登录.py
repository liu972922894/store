name = "root"
password = "admin"
cound = 0

while cound <= 3:
    cound = 0 + 1
    name1 = input("请输入用户名：")
    password1 = input("请输入密码：")
    if name1 == name and password1 == password:
        print("用户登录成功")
    elif name1 != name and password1 == password:
        print("用户名错误")
    elif name1 == name and password1 != password:
        print("密码错误")
    else:
        print("登录失败")
        break

