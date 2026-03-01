def my_decorator(fn_name):
    def fn_inner(x,y):
        print('正在努力计算中.....')
        return fn_name(x,y)
    return fn_inner


def get_sum(a,b):
    return a +b

get_sum = my_decorator(get_sum)
sum = get_sum(10,20)
print(sum)