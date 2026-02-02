# i = 0
# while i < 10:
#     print("hard study+" ,i+1)
#     i +=1

# i = 1
# sum = 0
# while i <=100:
#     sum +=i
#     i +=1
# print(f"sum的和是{sum}")

# import random
# num = random.randint(1,100)
#
# count = 0
# flag = True
#
# while flag:
#     guess_num = int(input("please enter your guessed number:"))
#     count +=1
#     if guess_num == num:
#         print("congratulation ,you are getting it right")
#         flag = False
#     else:
#         if guess_num >num:
#             print("your guessed num is too high")
#         else:
#             print("your guessed num is too low")
# print(count)

# import random
# num = random.randint(1,100)
#
# count=0
# flag = True
#
# while flag:
#     guess_num = int(input("enter your num:"))
#     count += 1
#     if guess_num == num:
#         print("you guessed right")
#
#         flag = False
#     else:
#         if guess_num >num:
#             print("the num is too high")
#         else:
#             print("the num is too low")
# print(f"count is {count}")


# i = 1
# while i<=10:
#     print(f"第{i}天，准备表白")
#
#     j =1
#     while j<=10:
#         print(f"送给小美的第{j}只玫瑰花")
#         j+=1
#     print("i love you xiaomei")
#     i += 1
#
# print(f"坚持到第{i-1}天，表白成功")


# i = 1
# while i <10:
#     j=1
#     while j <=i:
#         # 内层循环的print语句，不要换行，通过\t制表符进行对齐
#         print(f"{j}*{i}={j*i}\t", end='')
#         j += 1
#     i += 1
#     print()
#     # print空内容，就是输出一个换行

# i = 1
# while i <=9:
#     j = 1
#     while j<=i:
#         print(f"{j}*{i}={j*i}\t",end='')
#         j += 1
#     i += 1
#     print()

i=1
while i <= 9:
    j=1
    while j <=i:
        print(f"{j}*{i}={j*i}\t",end='')
        j+=1
    i+=1
    print()
