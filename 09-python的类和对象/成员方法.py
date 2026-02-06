
class student:
    name = None

    def say_hi(self,name):
       name = name
       print(self.name)
    def say_hello(self,msg):
        print(self.name,msg)

stu = student()
stu.say_hi("hello")
stu.name = '张三'

stu.say_hello("welcome to the jijinshichang")