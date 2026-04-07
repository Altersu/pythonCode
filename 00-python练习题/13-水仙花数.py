"""
水仙花数：是一个三位数，各位数字立方和等于该数字本身
"""
list =[]
for i in range(100,1000):
    if i == (i //100)**3 + (i//10%10)**3 + (i%10)**3:
        list.append(i)
print(list)
    # else:
    #     list1.append(i)
    #     print(list1)