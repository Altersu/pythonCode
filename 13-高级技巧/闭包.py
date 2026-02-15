"""
1️⃣ 栈帧与局部变量

当函数被调用时，Python 会创建一个 栈帧（Stack Frame）

栈帧里存放函数的局部变量、参数、指令指针等

函数执行完毕 → 栈帧销毁 → 局部变量释放

2️⃣ 内部函数捕获外部变量（闭包机制）

内部函数访问某个变量时，Python 按 LEGB 规则 查找：

Local（局部变量）

Enclosing（外层函数）

Global（全局变量）

Built-in（内建变量）

如果内部函数在局部找不到变量，会去外层函数找（Enclosing）

Python 会把这个变量存到一个 cell 对象 中

内部函数对象持有 指向 cell 的引用

外部函数执行完毕 → 栈帧消失，但 cell 在堆上，内部函数仍能访问

3️⃣ 闭包的底层理解

外部函数栈帧销毁 → 局部变量本来要释放

内部函数持有指向 cell 的指针 → cell 保存了原来的外部变量

内部函数返回给外部调用者 → 仍然可以访问闭包里的变量

"""




# # def outer(logo):
# #     def inner(msg):
# #         print(f"<{ logo}>{ msg}>{ logo}>")
# #     return inner
# #
# # fn1 = outer("*******")
# # fn1("股票涨起来")
# # fn1("有色起飞")
# #
# # fn2 = outer("@@@@@@@")
# # fn2("股票跌起来")
# # fn2("有色跌掉")
#
# # def outer(num1):
# #     def inner(num2):
# #         nonlocal num1
# #         num1 += num2
# #         print(num1)
# #     return inner
# # fn = outer(10)
# # fn(10)
# # fn(10)
# # fn(10)
#
#
# def account_create(initial_amount):
#     def atm(num,deposit=True):
#         nonlocal initial_amount
#         if deposit:
#             initial_amount += num
#             print(f"存款：+{num},账户余额：{initial_amount}")
#         else:
#             initial_amount -= num
#             print(f"取款：-{num},账户余额：{initial_amount}")
#     return atm
#
# atm1 = account_create(0)
# atm2 = account_create(0)
# atm1(100)
# atm2(100)
#
# # atm1(200)
# # atm1(300,False)



def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(20)
print(f.__closure__)      # 查看闭包
print(f.__closure__[0].cell_contents)  # x 的值
print(f(10))