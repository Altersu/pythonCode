# str1="wetyui"
# str2="congratulation"
# str3="approval"
# def my_len(data):
#     count = 0
#     for i in data:
#         count +=1
#     print(count)
# my_len(str1)
# my_len(str2)
# my_len(str3)

# def check( t):
#     if t < 37.5:
#         print(f"体温正常{t}，可以进入")
#     else:
#         print(f"体温异常{t}，需要隔离")
# check(39.3)


# def add(a,b):
#     result = a + b
#     return result
# r = add(5,7)
# print(r)

# def check_age(age):
#     if age > 18:
#         return "success"
#     else:
#         return None
# result = check_age(70)
# if not result:
#     print("donot in")


# def add(x,y):
#     """
#
#     :param x: 形参x表示相加的其中一个数字
#     :param y: 形参y表示相加的另一个数字
#     :return: 返回值是2数相加的结果
#     """
#
#     result = x + y
#     print(f"two num add is :{result}")
#     return result
# add(5,7)

# def func_b():
#     print("2")
#
# def func_a():
#     print("1")
#     func_b()
#     print("3")
#
# func_a()

# def test_a():
#     num = 100
#     print(num)
# test_a()

# num = 200
#
# def test_a():
#     print(f"test_a:{num}")
# def test_b():
#     global num
#     num =600
#     print(f"test_b:{num}")
#
# test_a()
# test_b()
# print(num)

# money = 5000000
# name = None
# name = input("please enter your name:")
#
# #　定义查询函数
#
# def query(show_header):
#     if show_header:
#         print("------------balance inquiry------------")
#     print(f"hello{name},your balance remaining{money}元")
#
# # 定义存款函数
# def saving(num):
#     global money
#     money += num
#     print("------------------deposit---------------------")
#     print(f"hello{name},your deposited {num}yuan")
#
#     #调用query函数查询余额
#     query(False)
# # 定义取款函数
# def get_money(num):
#     global money
#     money -= num
#     print("------------------withdrawal---------------------")
#     print(f"hello{name},your withdrew {num}yuan")
#
#     #调用query函数查询余额
#     query(False)
#
# #定义主菜单
# def main():
#     print("----------------primary menu----------------")
#     print(f"hello{name},Welcome to the bank ATM.please select your operation.")
#
#     print("balance inquiry \t\t[enter num 1]")
#     print("deposit \t\t\t\t[enter num 2]")
#     print("withdrawal \t\t\t\t[enter num 3]")
#     print("exit \t\t\t\t\t[enter num 4]")
#     return input("please enter your operation:")
#
# while True:
#     keyboard_input = main()
#     if keyboard_input == "1":
#         query(True)
#         continue # 通过continue继续下一次循环，一进来就是回到主菜单
#     elif keyboard_input == "2":
#         num = int(input("How much money do you want to deposit? Please enter"))
#         saving(num)
#         continue
#     elif keyboard_input == "3":
#         num = int(input("How much money do you want to withdraw? Please enter"))
#         get_money(num)
#         continue
#     else:
#         print("exit the programe")
#         break
#
#


# money = 5000
# name = input("请输入您的名字")
#
# def query(show_header):
#     if show_header:
#         print("------------balance inquiry------------")
#     print(f"hello {name},您的余额为{money}元")
#
# def saving(num):
#     global money
#     money +=num
#     print("------------------deposit---------------------")
#     print(f"hello{name},您要存款多少，请输入{num}")
#     query(False)
#
# def get_money(num):
#     global money
#     money -=num
#     print("------------------withdrawal---------------------")
#     print(f"hello{name},您要取多少钱，请输入{num}")
#     query(False)
#
# def main():
#     print("----------------primary menu----------------")
#     print(f"hello{name},欢迎来到银行ATM，请选择您的操作")
#     print("balance inquiry \t\t[enter num 1]")
#     print("deposit \t\t\t\t[enter num 2]")
#     print("withdrawal \t\t\t\t[enter num 3]")
#     print("exit \t\t\t\t\t[enter num 4]")
#     return input("请输入您的操作")
#
# while True:
#     keyinput = main()
#     if keyinput =="1":
#         query(True)
#         continue
#     elif keyinput == "2":
#         num = int(input("请输入您要存款的金额"))
#         saving(num)
#         continue
#     elif keyinput == "3":
#         num = int(input("请输入您要取款的金额"))
#         get_money(num)
#         continue
#     else:
#         print("退出程序")
#         break


# def test_return():
#     return 1,"hello",True
# x,y,z = test_return()
# print(x,y,z)


# def user_info(name,age,gender):
#     print(f"name:{name},age:{age},gender:{gender}")
# user_info(name='xiaosu',age=18,gender='girl')
# user_info(age=18,name='xiaosu',gender='girl')
# user_info('xiaosu',18,'girl')
# user_info('xiaosu',gender='girl',age=18)

# def user_info(*args):
#     print(args)
# user_info('xiaosu',18,'girl')
#
# def user_info(**kwargs):
#     print(kwargs)
# user_info(name='xiaosu',age=18,gender='girl')

# def test_func(compute):
#     result = compute(1,2)
#     print(type(compute))
#     print(result)
# def compute(x,y):
#     result = x*y
#     return result
# test_func(compute)

# def test_func(compute):
#     result = compute(1,2)
#     print(result)
# test_func(lambda x,y:x+y)



