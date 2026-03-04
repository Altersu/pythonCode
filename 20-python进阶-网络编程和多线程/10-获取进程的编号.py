"""
概述：
    在设备中，每个程序（进程）都有一个自己唯一进程id，当程序释放的时候，即：进程id是可以重复使用的
目的：
    查看子进程和父进程的关系，方便管理
    例如：杀死指定进程，创建子进程：
格式：
    查看当前进程的pid：
        os.getpid()
        multiprocessing.current_process().pid
    查看当前进程的ppid parent process id（父进程id）
        os.getppid()
细节：
    main中创建的进程，如果没有特殊指定，它的父进程都是main进程
    而main进程的父进程是pycharm程序的pid
"""


import time
import multiprocessing
import os
def coding(name,num):
    for i in range(1,num+1):
        time.sleep(0.1)
        print(f'{name}正在敲第{i}遍代码！')
    print(f'p1进程的pid:{os.getpid()},{multiprocessing.current_process().pid},父进程ppid:{os.getppid()}')
def music(name,num):
    for i in range(1,num+1):
        time.sleep(0.1)
        print(f'{name}正在听第{i}遍音乐！')
    print(f'p2进程的pid:{os.getpid()},{multiprocessing.current_process().pid},父进程ppid:{os.getppid()}')
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=coding,args=('小王',10))
    p2 = multiprocessing.Process(target=music,kwargs={'name':'xiaoming', 'num':10})
    p1.start()
    p2.start()
    print(f'主进程的pid:{os.getpid()},{multiprocessing.current_process().pid},父进程ppid:{os.getppid()}')