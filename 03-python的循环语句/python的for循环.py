# name = "wish you a good start"
# count = 0
# for x in name:
#     if x == "o":
#         count +=1
# print("count=",count)

# range 语法1 range(num)
# for x in range(10):
#     print(x,'\t',end='')
#

# for x in range(5,10):
#     print(x,'\t',end='')

# for x in range(5,10,2):
#     print(x, '\t', end='')

# count = 0
# for x in range(1,100):
#     if x%2==0:
#         count += 1
# print(f"有{count}个偶数")

# i = 1
# for i in range(1,11):
#     print(f"表白第{i}天")
#     for j in range(1,11):
#         print(f"送给消灭的第{j}朵玫瑰花")
#     print(f"第{i}天结束")
# print(f"第{i}天，表白成功")

# i=1
# for i in range(1,11):
#     print(f"表白第{i}天")
#     j=1
#     while j <=10:
#         print(f"送给消灭的第{j}朵玫瑰花")
#         j+=1
#     print(f"第{i}天结束")
# print(f"第{i}天，表白成功")

# i =1
# while i <=10:
#     print(f"表白第{i}天")
#     for j in range(1,11):
#         print(f"送给消灭的第{j}朵玫瑰花")
#     print(f"第{i}天结束")
#     i += 1
# print(f"第{i-1}天，表白成功")

# i =1
# for i in range(1,10):
#     j=1
#     while j <=i:
#         print(f"{j}*{i}={j*i}\t",end='')
#         j+=1
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={j * i}\t", end='')
#     print()

# for i in range(1,6):
#     print("1",end='')
#     for j in range (1,6):
#         print("2",end='')
#         break
#         print("3")
#     print('4',end='')
#     print()


money = 10000
import random


for i in range(1,21):
    score = random.randint(1, 10)
    if score <5:
        print(f"员工{i}地绩效分{score},不满足，不发工资，下一位")
        continue
    if money >=1000:
        money -= 1000
        print(f"员工{i},满足条件发放1000，余额{money}")
    else:
        print(f"{money}元，下个月再来")
        break

