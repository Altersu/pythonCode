# with open("csv_data/1.csv","w",encoding="utf-8") as f:
#     f.write("姓名,年龄,性别,爱好\n")
#     f.write("小王,18,男,'football,java'\n")
#     f.write("小李,18,女,python\n")
#     f.write("小张,20,男,Go\n")
#     f.write("小王,18,男,C++\n")
#
# with open("csv_data/1.csv","r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

import csv
# with open("csv_data/2.csv","w",encoding="utf-8",newline="") as f:
#     writer = csv.DictWriter(f,fieldnames=["姓名","年龄","性别","爱好"])
#     writer.writeheader()
#     writer.writerow({"姓名":"小王","年龄":18,"性别":"男","爱好":"python,java"})
#     writer.writerow({"姓名":"小帅","年龄":15,"性别":"男","爱好":"GO"})
#     writer.writerow({"姓名":"小美","年龄":19,"性别":"女","爱好":"Java"})
#     writer.writerow({"姓名":"小花","年龄":18,"性别":"女","爱好":"C++"})
#
with open("csv_data/2.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line)