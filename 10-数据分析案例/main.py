# """
# 面向对象，数据分析案例，主业务逻辑代码
# 实现步骤：
# 1. 设计一个类，可以完成数据的封装
# 2. 设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
# 3. 读取文件，生产数据对象
# 4. 进行数据需求的逻辑计算（计算每一天的销售额）
# 5. 通过PyEcharts进行图形绘制
# """
# from file_define import FileReader, TextFileReader, JsonFileReader
# from data_define import Record
# from pyecharts.charts import Bar
# from pyecharts.options import *
# from pyecharts.globals import ThemeType
#
# text_file_reader = TextFileReader("D:/2011年1月销售数据.txt")
# json_file_reader = JsonFileReader("D:/2011年2月销售数据JSON.txt")
#
# jan_data: list[Record] = text_file_reader.read_data()
# feb_data: list[Record] = json_file_reader.read_data()
# # 将2个月份的数据合并为1个list来存储
# all_data: list[Record] = jan_data + feb_data
#
# # 开始进行数据计算
# # {"2011-01-01": 1534, "2011-01-02": 300, "2011-01-03": 650}
# data_dict = {}
# for record in all_data:
#     if record.date in data_dict.keys():
#         # 当前日期已经有记录了，所以和老记录做累加即可
#         data_dict[record.date] += record.money
#     else:
#         data_dict[record.date] = record.money
#
# # 可视化图表开发
# bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
#
# bar.add_xaxis(list(data_dict.keys()))       # 添加x轴的数据
# bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))      # 添加了y轴数据
# bar.set_global_opts(
#     title_opts=TitleOpts(title="每日销售额")
# )
#
# bar.render("每日销售额柱状图.html")
#

"""
SQL 综合案例，读取文件，写入MySQL数据库中
"""
from file_define import TextFileReader, JsonFileReader
from data_define import Record
from pymysql import Connection
import json

text_file_reader = TextFileReader("D:/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("D:/2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
# 将2个月份的数据合并为1个list来存储
all_data: list[Record] = jan_data + feb_data

# 构建MySQL链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    autocommit=True
)
# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 组织SQL语句
# for record in all_data:
#     sql = f"insert into orders(order_date, order_id, money, province) " \
#           f"values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"
#     # 执行SQL语句
#     cursor.execute(sql)
cursor.execute("select * from orders")
result = cursor.fetchall()
dict_result = []
for i in result:
    dict_result.append({"date":i[0],
                        "order_id":i[1],
                        "money":i[2],
                        "province":i[3]})

# 写入 txt 文件，每条记录一行
# with open("D:/orders.txt", "w", encoding="utf-8") as f:
#     for row in dict_result:
#         f.write(str(row) + "\n")  # 直接把字典转成字符串写入


with open("D:/orders.txt", "w", encoding="utf-8") as f:
    for row in dict_result:
        d = row["date"]
        row["date"] = f"{d.year}, {d.month}, {d.day}"

        f.write(json.dumps(row, ensure_ascii=False) + "\n")




# with open("orders.txt", "w", encoding="utf-8") as f:
#     for row in dict_result:
#         f.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")

# 关闭MySQL链接对象
print(dict_result)
conn.close()



