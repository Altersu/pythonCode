"""
1.1个装饰器的参数有且只能有一个
2.如果装饰器有多个参数，可以在该装饰器外边在包裹一层，把该装饰器当作其内部函数

"""




def my_decorator(fn_name):
    def fn_inner(a,b):
        if fn_name.__name__ == 'get_sum':
            print('正在努力[加法]计算中...')
        elif fn_name.__name__ == 'get_sub':
            print('正在努力[减法]计算中...')
        return fn_name(a,b)
    return fn_inner


@my_decorator
def get_sum(a,b):
    return a+b
@my_decorator
def get_sub(a,b):
    return a-b

print(get_sum(10,30))
print('-'*34)
print(get_sub(66,30))
