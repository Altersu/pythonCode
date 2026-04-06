list = []
for i in range(1,100):
    if i % 2 != 0:
        list.append(i)
print(list)

# 第二种方法
list2= []
for i in range(1,100,2):
    list2.append(i)
print(list2)