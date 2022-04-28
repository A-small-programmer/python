num=input("请输入一个数字:")
j=len(num)-1
i=0
palind=True
while i<j:
    if num[i]!=num[j]:
        print("不是回文数")
        palind=False
        break
    else:
        i+=1
        j-=1
if palind:
    print("是回文数")
