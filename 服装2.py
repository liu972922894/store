id = (input("请输入身份证编号"))
name = (input("请输入姓名"))
sex = (input("请输入性别"))
heig = (input("请输入身高"))
add = (input("请输入居住地址"))

info = '''
-------------个人信息-------------
身份证编号：%s
姓名：%s
性别：%s
身高：%s
居住地址：%s 
---------------------------------
'''

print(info % (id,name,sex,heig,add))
