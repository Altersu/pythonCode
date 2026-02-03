# """
# 演示JSON数据和python字典的相互转换
# """
import json
# 准备列表，列表内每一个元素都是字典，将其转换为JSON数据
# data = [{"name":"张三","age":18},{"name":"王五","age":19},{"name":"赵六","age":20}]
# print(type(data))
# json_str = json.dumps(data,ensure_ascii=False)
# print(type(json_str))
# print(json_str)
# 准备字典，将字典转换为JSON
# d = {"name":"张三","age":18}
# print(type(d))
# json_str = json.dumps(d,ensure_ascii=False)
# print(type(json_str))
# print(json_str)
# # 将JSON字符串转换为python数据类型
# s = '[{"name":"张三","age":18},{"name":"王五","age":19},{"name":"赵六","age":20}]'
# print(type(s))
# l = json.loads(s)
# print(type(l))
# print(l)
#
# # 将JSON字符串转换为python数据类型
s = '{"name":"张三","age":18}'
d = json.loads(s)
print(type(d))
print(d)
