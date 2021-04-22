import random

nan = random.randint(1, 100)

count = 1
while True:
    count = count + 1
    nan1 = input("请输入你的数字")
    nan1 = int(nan1)
    if nan1 > nan:
        print("大了")
    elif nan1 < nan:
        print("小了")
    else:
        print("恭喜您，中奖了，中奖号码为：", nan, "您本次猜了",count, "次",)