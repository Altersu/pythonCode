import json
import random

# 基础数据类型注解
var1: int = 10
var2: str = "hello"
var3: bool = True

# 类对象类型注解
class Student:
    pass
stu: Student = Student()

# 基础容器类型注解
my_list: list = [1,2,3]
my_tuple: tuple = (1,2,3)
my_dict: dict = {"name":"张三","age":18}

# 容器类型详细注解
my_list: list[int] = [1,2,3]
my_tuple: tuple[int,str,bool] = (1,"2",True)
my_dict: dict[str,int] = {"name":"张三","age":18}

# 在注释中进行类型注解
# alt+enter键可以导包
var_1 = random.randint(1,10) # type: int
var_2 = json.loads('{"name":"zhangsan"}')  # type: dict
def func():
    pass
var_3 = func() # type: function
