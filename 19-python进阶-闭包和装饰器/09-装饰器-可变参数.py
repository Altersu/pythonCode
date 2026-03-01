def my_decorator(fn_name):
    def fn_inner(*args,**kwargs):
        print('正在努力计算中.....')
        return fn_name(*args,**kwargs)
    return fn_inner


@my_decorator
def get_sum(*args,**kwargs):

    sum = 0
    for i in args:
        sum += i

    for v in kwargs.values():
        sum += v
    return sum

    # 上述代码可以优化如下：
   # return sum( args)+sum(kwargs.values())


# get_sum = my_decorator(get_sum)
# sum =get_sum(10,20,30,a=100,b=200)
# print(sum)
sum = get_sum(10,20,30,a=100,b=200)
print(sum)