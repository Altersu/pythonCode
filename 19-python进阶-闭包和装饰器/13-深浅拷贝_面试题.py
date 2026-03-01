"""
1.所谓的深浅拷贝是指：
    浅拷贝：copy模块的copy（）
    深拷贝：copy模块的deepcopy（）
2.大白话解释深浅拷贝：
    深拷贝拷贝的多，浅拷贝拷贝的少
3.深浅拷贝注释是针对可变类型来讲的，深浅拷贝所有层（可变），浅拷贝只拷贝1层（可变）
如果是针对不可变类型，则用法和普通赋值一样，没啥区别


"""
import copy
def demo_1():
    # 普通赋值之不可变类型
    a = 10
    b =a
    print('id(a)---->',id(a))
    print('id(b)---->',id(b))
    print('id(10)---->',id(10))
    # 普通赋值之可变类型
    a = [1,2,3]
    b = [11,22,33]
    c = [a,b]
    d = c
    print('id(c)----->',id(c))
    print('id(d)----->',id(d))


# 浅拷贝之可变类型
def demo_2():

    a = [1,2,3]
    b = [11,22,33]
    c = [6,7,a,b]

    d = copy.copy(c)
    print('id(c)----->',id(c))
    print('id(d)----->',id(d))

    # 测试2
    print(id(c[2]))
    print(id(a))

    # 修改a[2] = 22
    a[2] = 22
    # c[0] = 100
    print('c----->',c)
    print('d----->',d)

# 浅拷贝不可变类型：不会给拷贝的对象C开辟新的内存空间，而只是拷贝了这个对象的引用
def demo_3():
    a =(1,2,3)
    b=(11,22,33)
    c=(6,7,a,b)

    d = copy.copy(c)
    print('id(c)----->',id(c))
    print('id(d)----->',id(d))

def demo_4():
    a = [1,2,3]
    b = [11,22,33]
    c = [6,7,a,b]
    d = copy.deepcopy(c)
    print('id(c)----->',id(c))
    print('id(d)----->',id(d))

    a[1] = 100
    b[1] = 800
    print(f'c: {c}')
    print(f'd: {d}')


# 深拷贝不可变类型：若为不可变类型直接就引用了，不开辟新的内存空间
def demo_5():
    a=(1,2,3)
    b=(11,22,33)
    c=(a,b)

    d = copy.deepcopy(c)
    print('id(c)----->',id(c))
    print('id(d)----->',id(d))

if __name__ == '__main__':

     # demo_1()
     # demo_2()
     # demo_3()
     # demo_4()
     demo_5()
