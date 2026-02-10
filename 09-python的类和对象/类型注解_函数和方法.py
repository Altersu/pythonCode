
# 对形参进行类型注解

def add(x:int,y:int):
    return x+y
# ctrl+p会弹出提示要输入的参数和类型
add()

# 对返回值进行类型注解
def func(data:list) -> list:
    return data
func()