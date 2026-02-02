# my_set = {1,1,1,66,6,88,66,6,99,88}
# my_set_empty = set()
# print(my_set)
# print(my_set_empty)
#
# my_set.add(1)
# my_set.add(10)
# print(my_set)
#
# my_set.remove(1)
# print(my_set)

# my_set = {66, 99, 6, 88,67}
# my_set.pop()
# print(my_set)
#
# my_set.clear()
# print(my_set)
#
#
# set1 = {1,2,3}
# set2 = {1,5,6}
# set3=set2.difference(set1)
# print(set1)
# print(set2)
# print(set3)
#
# set1 = {1,2,3}
# set2 = {1,5,6}
# set3=set1.difference_update(set2)
# print(set1)
# print(set2)

# set1 = {1,2,3}
# set2 = {1,5,6}
# set3=set2.union(set1)
# print(set1)
# print(set2)
# print(set3)
# num =len(set3)
# print(num)
#
# for ele in set3:
#     print(ele,end=' ')

my_list= ['黑马程序员','传智播客','黑马程序员','传智播客',
          'itheima','itcast','itheima','itcast','best']
my_set = set()
for ele in my_list:
    print(ele,end=' ')
    my_set.add(ele)
print()
print(my_set)

