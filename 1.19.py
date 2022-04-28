num1=int(input("请输入要计算的第一个数:"))
operator=input("请输入计算符号:")
num2=int(input("请输入要计算的第二个数:"))
if operator=="+":
    print(num1+num2)
elif operator=="*":
    print(num*num2)
elif operator=="-":
    print(num1-num2)
elif operator=="/":
    print(num1/num2)
else:
    print("只能输入加减乘除,请重新输入")

score=77
if score>=90 and score<=100:
    print("本次考试,等级为A")
elif score>=80 and score<80:
    print("本次考试,等级为B")
elif score>=70 and score<80:
    print("本次考试,等级为C")
elif score>=60 and score<70:
    print("本次考试,等级为D")
elif score>=0 and score<60:
    print("本次考试,等级为E")
