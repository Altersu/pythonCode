# print("欢迎来到迪士尼，儿童免费，成人280")
# # age = 30
# # input("input your age:")
# age = int(input("请输入您的年龄："))
# if age >= 18:
#     print("您已经成年，游玩需要买票")
# else:
#     print("你未成年，可以免费游玩")
# print("祝您游玩愉快")

# 友好的欢迎语
# print("欢迎来到迪士尼乐园！🎠")
# print("门票规则：18周岁及以下儿童免费，18周岁以上成人280元/人")
#
# # 异常处理：防止用户输入非数字内容
# try:
#     # 获取用户输入并转换为整数类型，同时赋值给age变量
#     age = int(input("\n请输入您的年龄："))
#
#     # 完整的条件判断逻辑
#     if  100> age > 18:
#         print(f"您的年龄是{age}岁，已成年，游玩需要购买门票（280元）。")
#     elif 0 <= age <= 18:
#         print(f"您的年龄是{age}岁，符合儿童免费政策，无需购票！")
#
#     elif age >100:
#         print(f"您的年龄是{age}岁，符合老人免费政策，无需购票！")
#     else:
#         print("年龄输入错误，请输入有效的正整数！")
# except ValueError:
#     # 处理用户输入非数字的情况
#     print("输入错误！请输入有效的数字（如 10、25）。")
#
# # 最终的祝福语
# print("祝您游玩愉快！😊")

# print("welcom to zoo!")
# high = int(input("please enter your height:"))
# if high >= 120:
#     print("您的身高超过120cm,游玩需要买票")
# else:
#     print("nindeshengaoweichaoguo120cm,buxuyaomaipiao")
# print("zhuninwandeyukuai")

# print("welcom to zoo")
# height = int(input("请输入您的身高（cm）："))
# vip_level=int(input("请输入您的vip等级（1~5）"))
# if height <120:
#     print("您的身高小于120cm，可以免费游玩")
# elif vip_level >3:
#     print("您的等级大于3，可以免费游玩")
# else:
#     print("您的条件都不满足，需要购票")
#
# print("祝您游玩愉快")

# num = 10
#
# if int(input("请猜一个数字:")) == num:
#     print("恭喜第一次就猜对了")
# elif int(input("猜错了，在猜一次:")) == num:
#     print("guess right")
# elif int(input("猜错了，再猜一次:")) == num:
#     print("恭喜，最后一次机会，你猜对了")
# else:
#     print("sorry you guess wrong")

# if int(input("what are you height:"))>120:
#     print("height over the limt,does not free")
#     print("if your level over the three,you can free")
#
#     if int(input("how are you level:")) > 3:
#         print("your level approval ,you can free")
#     else:
#         print("sorry,you need buy the ticket")
# else:
#     print("welcome the kids!")

# age = 11
# year = 1
# level = 5
# if age >18:
#     print("you are adult")
#     if age <30:
#         print("your age are approval")
#         if year > 2:
#             print(" your age and year are approval,you can take the prize")
#         elif level >3:
#             print("your age and level are approval,you can take the prize")
#         else:
#             print("your age and level dont reach the standard,you can not take the prize")
#     else:
#         print("your age are old")
# else:
#     print("your age are small,kid dont take the prize")

# import random
# num = random.randint(1,10)
#
# guess_num = int(input("please enter your guess num :"))
#
# if guess_num == num:
#     print("congratulation on getting in right on your first try")
# else:
#     if guess_num >num:
#         print("your guessed num is too high")
#     else:
#         print("your guessed number is too low")
#
#     guess_num = int(input("please enter the number you guessed agai："))
#     if guess_num == num:
#         print("congratulations,you guessed it right for the second time")
#     else:
#         if guess_num > num:
#             print("your guessed num is too high")
#         else:
#             print("your guessed num is too low")
#
#         guess_num = int(input("please enter the number you guessed again："))
#
#         if guess_num == num:
#             print("congratulation you guessed it right for the third time")
#
#         else:
#             if guess_num > num:
#                 print("your guessed num is to high")
#             else:
#                 print("your guessed num is to low")


import random
num = random.randint(1,10)

guess_num = int(input("please enter your guessed num:"))

if guess_num == num:
    print("congratulation on getting in right on your first try")
else:
    if guess_num > num:
        print("your guessed num is too high")
    else:
        print("your guessed num is too low")

    guess_num = int(input("enter your guessed number again:"))

    if guess_num == num:
        print("congratulations,your guessed it right for the second time" )
    else:
        if guess_num > num:
            print("the guessed num is too high")
        else:
            print("the guessed num is too low")

    guess_num = int(input("enter the guess num again:"))

    if guess_num == num:
        print("congratulations,you guessed it right for the third time")
    else:
        if guess_num > num:
            print("the guessed num is too high")
        else:
            print("the guessed num is too low")

