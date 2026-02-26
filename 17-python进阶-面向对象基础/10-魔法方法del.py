# """
# 案例: 演示 str魔法方法的 用法.
#
#
# 魔法方法:
#     概述/特点:
#         Python内置的函数, 在满足特定的场景下, 会被 自动调用.
#     常用的魔法方法:
#         __init__()      在(每次)创建对象的时候, 会自动触发该类的 __init__()函数.
#         __str__()       当用print()函数 打印对象的时候, 会自动调用该对象(所在类)的 str魔法方法.
#                         该魔法方法默认打印的是对象的地址值, 无意义, 一般都会重写, 改为打印 对象的各个属性值.
#         __del__()       当.py文件执行结束, 或者 手动 del 释放对象资源, 会自动调用该函数.
# """
#
# # 1. 定义汽车类, 属性: 品牌.   行为:run()   通过del魔法方法删除该类的对象, 看看效果.
# class Car:
#     # 2. 在魔法方法init中, 完成: 属性的初始化.
#     def __init__(self, brand):
#         self.brand = brand
#
#     # 3.重写 str魔法方法, 打印对象的属性值.
#     def __str__(self):
#         return f'品牌: {self.brand}'
#
#     # 4. 重写 del魔法方法, 删除对象时给出提示.
#     def __del__(self):
#         print(f'{self} 对象被删除了!')
#
#
# # 5. 创建汽车类对象.
# c1 = Car('小米 Su7 Ultra')
# print(c1)
#
# # 6. 手动访问 brand 属性.
# print(c1.brand)
# print('-' * 23)
#
# # 7.手动删除c1对象, 然后尝试 打印该对象 或者 访问对象的属性.
# # del c1
# # print(c1)       # 报错.
#
# print('程序结束!')

class Car:
    def __init__(self,brand):
        self.brand = brand

    def __str__(self):
        return f'{self.brand}'

    #  __del__()       当.py文件执行结束, 或者 手动 del 释放对象资源, 会自动调用该函数
    #　当程序执行结束以后，才会自动调用该函数
    #  或者手动删除，也会调用该函数，什么时候删除，什么时候调用
    def __del__(self):
        print(f'{self}被删除了')

c1 = Car('奔驰e300')
print(c1)
print('-'* 36)
# del c1
print('程序结束')