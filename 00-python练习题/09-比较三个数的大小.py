"""
输入三个数，从小到达输出三个数

"""
a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))
c = int(input("请输入第三个数字："))

list=[a,b,c]
list1 = sorted(list)
print(list1)
print("三个数字从小到大的顺序是：",list1[0],list1[1],list1[2])

