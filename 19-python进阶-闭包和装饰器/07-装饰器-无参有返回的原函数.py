def my_decorator(fn_name):
    def fn_inner():
        print('正在努力计算中.....')
        return fn_name()
    return fn_inner

def get_sum():
    a =11
    b =22
    return a+b

get_sum = my_decorator(get_sum)
sum = get_sum()
print(sum)