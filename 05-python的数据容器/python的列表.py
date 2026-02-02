# # my_list = ["alter",666,True]
# # print(my_list)
# # print(my_list[0])
# # print(my_list[1])
# # print(my_list[2])
# # print(my_list[-1])
# # print(my_list[-2])
# # print(my_list[-3])
# # print(type(my_list))
#
# # my_list = [[1,2,3],[4,5,6]]
# # print(my_list[0][1])
# # print(my_list[1][1])
#
# # def add(a,b):
# #     result = a + b
# #     return result
# # sum=add(5,7)
# # print(sum)
#
# my_list=["alter","jiayou","happy"]
# index=my_list.index("jiayou")
# print(f"索引值是:{index}")
#
# #修改元素
# my_list[1]="progress"
# print(my_list[1])
#
# #插入元素
# my_list.insert(1,"best")
# print(my_list)
#
# # 追加单个元素
# my_list.append("better")
# print(my_list)
#
# # 追加一批元素
# mylist=[1,2,3]
# my_list.extend(mylist)
# print(my_list)
#
# # 删除元素
# del my_list[-1]
# print(my_list)
#
# element = my_list.pop(-1)
# print(my_list,element)
#
# my_list.remove(1)
# print(my_list)
#
# # 清空列表
# # my_list.clear()
# # print(my_list)
#
# my_list.insert(2,"best")
# print(my_list)
# count =my_list.count("best")
# print(count)
#
# count =len(my_list)
# print(count)
#
#
# print(my_list.index("best"))

# mylist=[21,25,21,23,22,20]
# mylist.append(31)
# print(mylist)
# mylist2=[29,33,30]
# mylist.extend(mylist2)
# print(mylist)
# print(mylist[0])
# print(mylist[-1])
#
# index=mylist.index(31)
# print(index)

# def list_while_func():
#     mylist=["alter","best","better"]
#     index = 0
#     while index < len(mylist):
#         element = mylist[index]
#         print(element)
#         index +=1
# list_while_func()
#
# def list_for_func():
#     mylist1=["mine","van","notion"]
#     # for index in range(len(mylist1)):
#     #     element = mylist1[index]
#     #     print(element)
#     #     index +=1
#     for element in mylist1:
#         print(element)
# list_for_func()


def while_func():
    mylist=[1,2,3,4,5,6,7,8,9,10]
    mylist1 = []
    index = 0
    while index < len(mylist):
        element = mylist[index]
        if element %2 == 0:
            mylist1.append(element)
        index +=1
    print(mylist1)
while_func()

def for_func():
    mylist=[1,2,3,4,5,6,7,8,9,10]
    mylist1 = []
    for element in mylist:
       if element %2 == 0:
           mylist1.append(element)
    print(mylist1)

for_func()