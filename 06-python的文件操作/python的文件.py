import time

# f = open("C:/Users/sumen/Desktop/基金.txt","r",encoding="utf-8")
# print(type(f))
# 读取文件
# print(f.read(8))
# print(f.read())

# 读取文件的全部行，封装到列表中
# lines = f.readlines()
# print({type(lines)})
# print(lines)

# 读取文件

# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(line1)
# print(line2)
# print(line3)

# for line in f:
#     print(line)
# f.colse()

# with open("C:/Users/sumen/Desktop/基金.txt","r",encoding="utf-8") as f:
#     for line in f:
#         print(line)
# time.sleep(60)

f = open("C:/Users/sumen/Desktop/基金.txt","r",encoding="utf-8")

# content = f.read()
# # print(content)
# count = content.count("itheima")
# print(count)

# count = 0
# for line in f:
#     line = line.strip() # 去除开头和结尾的空格以及换行符
#     words = line.split(" ")
#     # print( words)
#     for word in words:
#         if word == 'itheima':
#             count +=1
# print(count)

# f = open("C:/Users/sumen/Desktop/test.txt","a",encoding="utf-8")
# f.write("hello world") # 将内容写入内存中
# # f.flush() # 将内存中积攒的内容，写入到硬盘的文件中
# f.close() # close方法，内置了flush的功能的

# f = open("C:/Users/sumen/Desktop/test.txt","a",encoding="utf-8")
# f.write("\nyousezhangqilai") # 将内容写入内存中
# # f.flush() # 将内存中积攒的内容，写入到硬盘的文件中
# f.close()

# fr = open("C:/Users/sumen/Desktop/test.txt","r",encoding="utf-8")
# fw = open("C:/Users/sumen/Desktop/test1.txt.bak","w",encoding="utf-8")
#
# for line in fr:
#     line = line.strip()
#     # 判断内容，将满足的内容写出
#     if line.split(",")[4] == "测试":
#         continue # continue进入下一次循环，这一次后面的内容就跳过了
#     # 将内容写出
#     fw.write(line)
#     # 由于前面对内容进行了strip()的操作，所以要动手写出换行符
#     fw.write("\n")
#
#
# fr.close()
# fw.close()

