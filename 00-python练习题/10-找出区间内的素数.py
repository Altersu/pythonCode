"""
输入整数a,b表示一个闭区间
找出该区间内的所有素数并打印
"""
# a = int(input("请输入一个数字："))
# b = int(input("请输入一个数字："))
# list = []
# for i in range(a,b+1):
#     for j in range(2,i):
#         if i % j ==0:
#             break
#     else:
#         list.append(i)
# print(list)
a = int(input("请输入一个数字："))
b = int(input("请输入一个数字："))
list = []
for i in range(a,b+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        list.append(i)
print(list)

def prime(n):
    flag = True
    for i in range(2,n):
        if n % i == 0:
            flag = False
            break
    return flag
a = int(input("请输入一个数字："))
b = int(input("请输入一个数字："))
list = []
for i in range(a,b+1):
    if prime(i):
        list.append(i)
print(list)