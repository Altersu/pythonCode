
from studentcms_oop.student import Student

s1 = Student('德桦', '男', 81, '111', '刻骨铭心')
print(s1)

my_dict = s1.__dict__
print(my_dict)
print(type(my_dict))

print('-'*  23)
s1 = Student('德桦', '男', 81, '111', '刻骨铭心')
s2 = Student('志奇', '男', 22, '222', '我不是紫琦')
s3 = Student('紫琦', '男', 66, '333', '有请志奇')
stu_list = [s1, s2, s3]

# list_dict =[]
# for stu in stu_list:
#     list_dict.append(stu.__dict__)
# print(list_dict)

# 列表推导式
list_dict = [stu.__dict__ for stu in stu_list]
print(list_dict)

print('-'*  23)

# 需求3: 把 {'name': '德桦', 'gender': '男', 'age': 81, 'phone': '111', 'desc': '刻骨铭心'} -&gt; 学生对象
my_dict = {'name': '德桦', 'gender': '男', 'age': 81, 'phone': '111', 'desc': '刻骨铭心'}
s5 = Student(my_dict['name'], my_dict['gender'], my_dict['age'], my_dict['phone'], my_dict['desc'])
print(s5)

s6 = Student(**my_dict)
print(s6)
print(type(s6))