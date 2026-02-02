# my_list = [0,1,2,3,4,5,6]
# result1 = my_list[1:4]
# print(result1)
#
# my_tuple = (0,1,2,3,4,5,6)
# result2 = my_tuple[:]
# print(result2)
#
# my_str = "0123456"
# result3 = my_str[::2]
# print(result3)
#
# my_str = "0123456"
# result4 = my_str[::-1]
# print(result4)
#
# my_tuple = (0,1,2,3,4,5,6)
# result5 = my_tuple[::-2]
# print(result5)
#
# my_list = [0,1,2,3,4,5,6]
# result6 = my_list[3:0:-1]
# print(result6)

mystr = "万过薪月，员序程马黑来，nohtyp学"
# name = mystr[9:4:-1]
# print(name)
#
# new_mystr = mystr.split("，")
# print(new_mystr)
# news= new_mystr[1]
# new = news.replace("来"," ")
# print(new)
# renew = new[::-1]
# print(renew)

result1 = mystr[::-1][9:14]
print(result1)

result2 = mystr[5:10][::-1]
print(result2)

result3 =mystr.split("，")[1].replace("来","")[::-1]
print(result3)