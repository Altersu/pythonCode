import json

user = {
    "name":"alter",
    "age":18,
    "gender":"girl",
    "hobby":["reading","swimming"]
}

# with open("resources/user.json","w",encoding="utf-8")as f:
#     json.dump(user,f ,ensure_ascii=False,indent=2)
    # ensure_ascii默认值是true，确保所有的数据输出的数据都是ascii编码,非ASCII码会进行转义，false，非ASCII码保留原样输出
    # indent参数，指定缩进量，默认是None，不缩进，指定缩进量，则格式化输出

# with 语句（上下文管理器）的核心作用就是确保资源总是正确获取和释放
# 即使发生异常，也会被正常释放，也是项目开发中的推荐方式

# 读取json数据文件

with open("resources/user.json","r",encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))