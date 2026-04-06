"""
素数指的是在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数
"""
# num = int(input("请输入一个数字："))
# for i in range(2,num):
#     if num % i == 0:
#         print("不是素数")
#         break
# else:
#     print("是素数")

# num = int(input("请输入一个数字:"))
# flag = False
# for i in range(2,num):
#     if num % i ==0:
#         flag = True
#         break
# if flag:
#     print("不是素数")
# else:
#     print("是素数")

num = int(input("请输入一个数字:"))
for i in range(2,num):
    if num % i == 0:
        print("不是素数")
        break
else:
    print("是素数")