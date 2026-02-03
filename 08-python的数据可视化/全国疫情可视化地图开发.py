
import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts,TitleOpts

def normalize_province_name(name: str) -> str:
    # 直辖市
    municipalities = {"北京", "上海", "天津", "重庆"}

    # 自治区
    autonomous_regions = {
        "内蒙古": "内蒙古自治区",
        "广西": "广西壮族自治区",
        "西藏": "西藏自治区",
        "宁夏": "宁夏回族自治区",
        "新疆": "新疆维吾尔自治区",
    }

    # 特别行政区
    special_regions = {
        "香港": "香港特别行政区",
        "澳门": "澳门特别行政区",
    }

    if name in municipalities:
        return name + "市"
    elif name in autonomous_regions:
        return autonomous_regions[name]
    elif name in special_regions:
        return special_regions[name]
    else:
        return name + "省"


f = open("D:/疫情.txt","r",encoding="utf-8")
data = f.read()
f.close()
data_dict = json.loads(data)
province_data_list = data_dict['areaTree'][0]["children"]

data_list = []

for province_data in province_data_list:
    raw_name = province_data["name"]
    province_name = normalize_province_name(raw_name)
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))



map=Map()
map.add("各省份确诊人数",data_list,"china")
map.set_global_opts(
    title_opts = TitleOpts(title="全国疫情地图"),
    visualmap_opts = VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1-99人","color":"#CCFFFF"},
            {"min":100,"max":999,"label":"100-999人","color":"#FF6666"},
            {"min":1000,"max":4999,"label":"1000-4999人","color":"#990033"},
            {"min":5000,"max":9999,"label":"5000-9999人","color":"#6600CC"},
            {"min":10000,"max":99999,"label":"10000-99999人","color":"#CC00FF"},
            {"min":100000,"label":"100000-999999人","color":"#FF00FF"},
        ]
    )
)

map.render("全国疫情地图.html")