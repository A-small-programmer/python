import random
number=random.randint(1,100)
while True:
    num=int(input("请输入你猜的数字:"))
    if num==number:
        print("猜中了")
        break
    elif num>number:
        print("猜大了")
    else:
        print("猜小了")
