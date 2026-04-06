"""
输入两个直角边长，求出三角形协变的长度
"""
a = int(input("请输入直角三角形的边长："))
b = int(input("请输入直角三角形的边长："))
c = (a**2 +b**2 )**0.5
print("三角形的斜边长为：",c)

import math
a = int(input("请输入直角三角形的边长："))
b = int(input("请输入直角三角形的边长："))
c = math.sqrt(a**2 +b**2 )
print("三角形的斜边长为：",c)