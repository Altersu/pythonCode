
from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(['us','jp','China'])
bar1.add_yaxis("GDP",[10,20,30],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(['us','jp','China'])
bar2.add_yaxis("GDP",[20,30,60],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(['us','jp','China'])
bar3.add_yaxis("GDP",[30,40,90],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

timeline = Timeline(
    {"theme":ThemeType.LIGHT}
)
# 在时间线内添加柱状图对象
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")

timeline.add_schema(
    play_interval=1000, # 自动播放时间间隔，单位毫秒
    is_loop_play=True,  # 是否在自动播放的时候，显示时间线
    is_auto_play=True,  # 是否自动播放
    is_timeline_show=True # 是否循环自动播放
)


timeline.render("基础时间线柱状图.html")