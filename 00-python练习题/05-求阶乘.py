"""
一个正整数的阶乘是所有小于及等于该数的正整数的积
并且0的阶乘为1
自然数n的阶乘写作n!
"""
num = int(input("请输入一个正整数："))
result = 1
for i in range(1,num+1):
    result *= i
print(result)
def jiecheng(num):
    if num == 1:
        return 1
    else:
        return num*jiecheng(num-1)
print(jiecheng(num))