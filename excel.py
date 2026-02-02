import pandas as pd

# 读取原始表（注意文件名）
# df = pd.read_excel('副本省属.xlsx', header=1)
# 使用完整路径
df = pd.read_excel(r'C:\Users\sumen\Desktop\事业编\副本省属.xlsx', header=1)

df.columns = [
    '序号','事业单位','主管部门','岗位类别','岗位等级','岗位性质','岗位名称',
    '招聘人数','学历要求','学位要求','专科专业要求','本科专业要求','研究生专业要求',
    '其他条件','开考比例','成绩比例','咨询电话','备注'
]

# 1. 学历：本科及以上
mask_edu = df['学历要求'].astype(str).str.contains('本科')

# 2. 本科计算机相关专业
keywords = [
    '计算机','软件','网络','信息','数据',
    '人工智能','电子','通信','自动化','数字'
]
pattern = '|'.join(keywords)

mask_major = (
    df['本科专业要求'].isna() |
    df['本科专业要求'].astype(str).str.contains(pattern)
)

result = df[mask_edu & mask_major]

# 导出新 Excel
result.to_excel('本科计算机专业可报考岗位.xlsx', index=False)

print('生成完成')
