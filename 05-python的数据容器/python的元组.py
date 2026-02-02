

# t1 = (1,"hello",True)
# t2 = ()
# t3 = tuple()
# print(type(t1),t1)
# print(type(t2),t2)
# print(type(t3),t3)
#
# t4 = ("youse", )
# print(type(t4),t4)
#
# t5 = ((1,2,3),(1,2,3))
# print(type(t5),t5)
#
# num = t5[1][2]
# print(num)
#
#
# t6 = ("youse","zijin","luomu")
# index = t6.index("youse")
# print(index)
#
# t7 = ("youse","zijin","luomu","youse","youse")
# count =t7.count("youse")
# print(count)

# t8 = ("youse","zijin","luomu","youse","youse")
# num = len(t8)
# print(num)
#
# index = 0
# while index < len(t8):
#     element = t8[index]
#     print(element)
#     index +=1
#
# for element in t8:
#     print(element)

# t9 = (1,2,["yousebizhang","huitiao"])
# print(t9)
# t9[2][0] ="youse"
# t9[2][1] = "zhang"
# print(t9)

t = ('周杰伦',11,["football",'music'])
index = t.index(11)
print(index)

name = t[0]
print(name)

list = t[2]
del list[0]
print(t)

list.append("coding")
print(t)