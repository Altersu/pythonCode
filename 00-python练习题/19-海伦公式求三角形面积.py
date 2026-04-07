"""
海伦公式是利用三角形的三条边的边长直接
求三角形面积的公司
"""
import math
a = int(input("请输入三角形的边长："))
b = int(input("请输入三角形的边长："))
c = int(input("请输入三角形的边长："))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
area1 = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("三角形的面积为：",area)
