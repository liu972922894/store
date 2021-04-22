a = int(input("a边："))
b = int(input("b边："))
c = int(input("c边："))


if a == b == c:
    print("可以构成等边三角形")
elif a == b or b == c or c == a:
    print("可以构成等腰三角形")
elif a^2+b^2==c^2:
    print("可以构成直角三角形")

elif a + b > c and a + b > c and b + c > a:
    print("可以构成三角形")
else:
    print("不能构成三角形")
