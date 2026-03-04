"""
进程的特点：
    1.数据之间是相互隔离的
        因为子进程相当于是父进程的“副本”，会将父进程的"main外资源“拷贝一份
    2.默认情况下，主进程会等待子进程执行结束后结束：
        如果要设置主进程结束，子进程同步结束，方式如下：
        1.思路一设置子进程为守护进程
        2.思路二：强制关闭子进程，可能会导致子进程变成僵尸进程，交由python解释器自动回收
          （底层有init初始化进程来管理维护）
"""
import multiprocessing
import time

def work():
    for i in range(10):
        print('正在努力工作')
        time.sleep(0.2)

if __name__ == '__main__':
    p1= multiprocessing.Process(target=work)
    # 思路一 设置p1为守护进程
    p1.daemon= True
    p1.start()
    time.sleep(1)

    # 思路2：强制关闭子进程
    # p1.terminate()
    print('主进程结束')