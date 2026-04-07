"""
输入一个正整数，输出她的所有质数因子
如180的质数因子为2，2，3，3，5
"""
list = []
a= int(input("请输入一个正整数:"))
y= 2
while a != y:
    if a %y== 0:
        list.append(y)
        a /= y
    else:
        y +=1
list.append(int(a))
for i in list:
    print(i ,end=' ')
