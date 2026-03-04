"""

线程和进程的关系：
    1.进程是CPU分配资源的基本单位，线程是CPU调度资源的最小单位
    2.线程是依附于进程的，每个进程至少有1个线程（主线程）
    3.进程间数据相互隔离，（同一个进程的）线程间数据可以共享
"""
import threading,time
def coding():
    for i in range(1,6):
        time.sleep(0.1)
        print(f'正在敲第{i}遍代码！')


def music():
    for i in range(1,6):
        time.sleep(0.1)
        print(f'正在听第{i}遍音乐~~~~~~~~')

if __name__ == '__main__':

    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=music)
    t1.start()
    t2.start()