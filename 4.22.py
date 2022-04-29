var=5
while var>0:
    var=var-1
    if var==3:
        continue
    print("当前变量值:",var)
print("Good bye")

var=5
while var>0:
    var=var-1
    if var==3:
        break
    print("当前变量值:",var)
print("Good bye")

i=1
while i<10:
    i+=1
    if i%2>0:
        continue
    print(i)

for letter in "python":
    if letter=="h":
        continue
    print("当前字母:",letter)

num=0
x=0
while 1:
    x=x+1
    if x>100:
        break
    if x%2==0:
        continue
    num+=x
print(num)
