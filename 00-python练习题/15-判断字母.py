"""
输入字符，判断是否为字母
"""
a = input("请输入一个字符：")
result = a.isalpha()
if result :
    print("是字母")
else:
    print("不是字母")