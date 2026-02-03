
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
line = Line()
line.add_xaxis(["美国","俄罗斯","中国"])
line.add_yaxis("GDP",[10,20,30])
# 设置全局配置项set_global_opts来展示
line.set_global_opts(
    # 按 Ctrl + P 看到的是 函数签名提示（Parameter Info / 参数信息）
    title_opts=TitleOpts(title="GDP展示",pos_left ="center",pos_bottom="1%"),
    # 图例
    legend_opts = LegendOpts(is_show=True),
    # 工具箱
    toolbox_opts = ToolboxOpts(is_show=True),
    # 视觉映射
    visualmap_opts = VisualMapOpts(is_show=True)
)
# 通过render方法，将代码生成为图像
line.render()