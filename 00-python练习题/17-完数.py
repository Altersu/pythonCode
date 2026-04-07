"""
一个数恰好等于除了它以外的因子之和，这个数就成为"完数"
编程序找出1000以内的所有完数
6是一个完数，她的因子是1，2，3
"""
list = []
for i in range(1,1001):
    sum = 0
    for j in range(1,i):
        if i % j == 0:
            sum += j
    if sum == i:
        list.append(i)
print(list)

for i in range(1,1000):
    sum = 0
    for j in range(1,i):
        if i % j == 0:
            sum += j
    if sum == i:
        print(i)