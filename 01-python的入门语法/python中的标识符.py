# 规则1：内容限定，限定只能使用:中文，英文，数字，下划线，注意：不能以数字开头
# 错误的代码示范 1_name = "张三“
# 错误的代码示范：name_! = "张三"
name_1 = "alter"
_name = "xiaosu"
name_ = "red"

# 规则2： 大小写敏感
Alter = "xiaoming"
alter = 888
print(Alter,alter)

#规则3：不可使用关键字
# 错误的示范 class = 1 , def = 2
Class = 1