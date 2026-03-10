"""
property属性介绍：
    作用：
        把 函数 当做变量来使用
    实现方式：
        方式1：装饰器
        方式2：类属性
property的装饰器用法：
    @property             修饰 获取值的函数
    @获取值的函数名.setter   修饰 设置值的函数

    装饰之后，就可以直接 .上述的函数名 来当作变量直接用

"""
class Student:
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age = age


if __name__ == '__main__':
    s = Student()
    s.age = 20
    print(s.age)