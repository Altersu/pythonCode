#
# class student:
#     """
#      定义的成员变量可以省略
#     """
#     name = None
#     age = None
#     tel = None
#     def __init__(self,name,age,tel):
#         self.name = name
#         self.age = age
#         self.tel = tel
#         print("自动执行")
# stu = student("张三",18,"123456")
# print(stu.name,stu.age,stu.tel)


# class student:
#
#     def __init__(self,name,age,address):
#         for i in range(2):
#             print(f"当前录入第{i+1}个学生信息：，总共需要录入10位学生信息")
#             self.name = input("请输入姓名：")
#             self.age = input("请输入年龄：")
#             self.address = input("请输入地址：")
#             print(f"学生{i+1}信息录入完成，信息为：【学生姓名：{self.name}，学生年龄：{self.age}，学生地址：{self.address}】")
#
# stu = student(None,None,None)

class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    # __str__魔术方法
    def __str__(self):
        return f"学生姓名：{self.name}，学生年龄：{self.age}"
    # --lt__魔术方法
    def __lt__(self,other):
        return self.age < other.age
    #__le__魔术方法
    def __le__(self,other):
        return self.age <= other.age
    #__eq__魔术方法
    def __eq__(self,other):
        return self.age == other.age



stu1 = student("张三",35)
stu2 = student("李四",19)
print(stu1 == stu2)
print(stu1 >= stu2)