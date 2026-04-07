"""
输入一个四位数，反向输出对应的四位数
"""
# list = []
# for i in range(1000,10000):
#     a = i // 1000
#     b = i //100 %10
#     c = i // 10 % 10
#     d = i % 10
#     print(f'{d}{c}{b}{a}')

i= int(input("请输入一个四数字："))
a = i // 1000
b = i //100 %10
c = i // 10 % 10
d = i % 10
print(f'{d}{c}{b}{a}')

a= int(input("请输入一个数字："))
a = str(a)
a = a[::-1]
a = int(a)
print(a)



