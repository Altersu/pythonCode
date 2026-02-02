
# my_str = "youse kending hui shangzhang"
# value = my_str[6]
# print(value)
#
# value = my_str.index("hui")
# print(value)
#
# new_str = my_str.replace("hui","biding")
# print(my_str)
# print(new_str)
#
# my_str_list = my_str.split(" ")
# print(my_str_list)
#
# mystr= "  youse bingding shangzhang  "
# new_mystr = mystr.strip()
# print(new_mystr)

# mystr= "12youse bingding shangzhang21"
# new_mystr = mystr.strip("12")
# print(new_mystr)
# count = mystr.count("ng")
# print(count)
# num = len(mystr)
# print(num)
#
# index = 0
# while index < len(mystr):
#     element = mystr[index]
#     print(element,end='')
#     index +=1
# print()
# for element in mystr:
#     print(element,end='')

# str = "jinshu doude zhang changqi kanhao zijin he youse"
# count = str.count("n")
# print(count)
#
# new_str = str.replace(" ","|")
# print(new_str)
#
# split_new_str = new_str.split("|")
# print(split_new_str)
# # split_new_str = new_str.split()
# # print(split_new_str)
# # new_str = str.split("|")
# # print(new_str)
# new_str = str.split()
# print(new_str)

str = "jinshu doude zhang changqi kanhao zijin he youse"
new_str = str.replace(" ","|")  # new_str → 指向替换后的字符串（如jinshu|doude|...）
print(new_str)
new_str = str.split("|")        # new_str → 重新指向分割后的单元素列表，原字符串被覆盖
print(new_str)
new_str = str.split()           # new_str → 再次重新指向空格分割后的多元素列表，原列表被覆盖
print(new_str)                  # 最终打印最后一次赋值的结果

mystr = "itheima itcast boxuegu"
count = mystr.count("it")
print(count)

new_mystr = mystr.replace(" " ,"|")
print(new_mystr)

new = new_mystr.split("|")
print(new)