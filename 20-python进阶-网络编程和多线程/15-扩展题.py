"""
需求：
    问1，2，3，4能组合的四位数有几种情况，按照5个一行输出
要求：
    1.要求同时包含1，2，3，4这四个数字
        1234，1324
    2.要求数字1和3不能挨着
        1234，3412
    3.数字4不能开头
    4.5行以内搞定（包括5行）
思路：
    把数字转化成字符串，然后调用字符串的功能做判断，即可
"""
# count = 0
# for i in range(1234,4321+1):
#     s = str(i)
#     if '1' in s and '2' in s and '3' in s and '4' in s:
#         count += 1
#
#         print(s,end="\n" if count %5 == 0 else '\t')

# count = 0
# for i in range(1234,4321+1):
#     s =str(i)
#     if '1' in s and '2' in s and '3' in s and '4' in s and '13' not in s and '31' not in s:
#         count += 1
#         print(s,end="\n" if count %5 == 0 else '\t')

# count = 0
# for i in range(1234,4321+1):
#     s =str(i)
#     if '1' in s and '2' in s and '3' in s and '4' in s and s[0]!= '4':
#         count += 1
#         print(s,end="\n" if count %5 == 0 else '\t')

# count = 0
# for s in [str(i) for i in range(1234,4322)]:
#     if '1' in s and '2' in s and '3' in s and '4' in s:
#         count += 1
#         print(s,end="\n" if count %5 == 0 else '\t')
#
print([int(s) for s in [str(i) for i in range(1234,4322)]if '1' in s and '2' in s and '3' in s and '4' in s])


my_list = ['aa','bb','cc','bb','bb','bb','dd']
# 切片的底层逻辑就是浅拷贝
for s in my_list[:]:
    if s == 'bb':
        my_list.remove(s)
print(my_list)