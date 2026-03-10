"""
生成器介绍：
    概述：
        所谓的生成器就是基于数据规则，用一部分在生成一部分，而不是一下子生成玩所有
    目的：
        可以节省大量的内存
    实现方式：
        1.推导式写法
        2.yield关键字
"""
import sys

my_generator = (i for i in range(1,11))
print(my_generator)
print(type(my_generator))
print('-'*23)

my_gt2 = (i for i in range(1,11) if i % 2 == 0)
print(my_gt2)
print('-'*23)

print(next(my_gt2))
print(next(my_gt2))
print('-'*23)

for i in my_gt2:
    print(i)

print('-'*23)

my_list = [i for i in range(1000000)]
my_gt3 = (i for i in range(1000000))
print(type(my_list), type(my_gt3))

print(sys.getsizeof(my_list), sys.getsizeof(my_gt3))