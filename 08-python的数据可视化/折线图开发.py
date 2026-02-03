
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts,LegendOpts,ToolboxOpts,VisualMapOpts



f_us = open("D:/美国.txt","r",encoding="utf-8")
us_data = f_us.read() # 读取全部内容和

f_jp = open("D:/日本.txt","r",encoding="utf-8")
jp_data = f_jp.read() # 读取全部内容和

f_in = open("D:/印度.txt","r",encoding="utf-8")
in_data = f_in.read() # 读取全部内容和

# 去掉不合  JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(","")
jp_data = jp_data.replace("jsonp_1629350871167_29498(","")
in_data = in_data.replace("jsonp_1629350745930_63180(","")


# 去掉不合  JSON规范的结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]


# json转python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

us_trend_data = us_dict["data"][0]["trend"]
us_x_data = us_trend_data['updateDate'][:314]
us_y_data = us_trend_data['list'][0]['data'][:314]

jp_trend_data = jp_dict['data'][0]['trend']
jp_x_data = jp_trend_data['updateDate'][:314]
ji_y_data = jp_trend_data['list'][0]['data'][:314]

in_trend_data = in_dict['data'][0]['trend']
in_x_data = in_trend_data['updateDate'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

line = Line()

# x轴是公用的，所以使用一个国家的数据即可
line.add_xaxis(us_x_data)

# label_opts = LabelOpts(is_show=False 折线上的数据不显示
line.add_yaxis("美国确诊人数",us_y_data,label_opts = LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数",ji_y_data,label_opts = LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数",in_y_data,label_opts = LabelOpts(is_show=False))

line.set_global_opts(
    title_opts = TitleOpts(title="2020年美日印三国确诊人数对比折线图",
                           pos_left = "center",pos_bottom="1%")
)


line.render()

f_us.close()
f_jp.close()
f_in.close()