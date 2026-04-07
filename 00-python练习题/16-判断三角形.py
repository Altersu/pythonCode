"""
输入三组数据，判断能否构成三角形的三条边
"""
# a = int(input("请输入三角形的边长："))
# b = int(input("请输入三角形的边长："))
# c = int(input("请输入三角形的边长："))
# if a + b > c and a + c > b and b + c > a:
#     print("可以构成三角形")
# else:
#     print("不能构成三角形")
a=int(input("请输入三角形的边长："))
b=int(input("请输入三角形的边长："))
c=int(input("请输入三角形的边长："))
if a<=0 or b<=0 or c<=0:
    print("不能构成三角形")
    exit()
if a+b >c and a+c >b and b+c >a :
    print("可以构成三角形")
else:
    print("不能构成三角形")