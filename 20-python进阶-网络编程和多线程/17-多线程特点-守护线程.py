"""
多线程特点：
    1.线程执行具有随机性，原因是因为CPU在做着高效的切换
    2.默认情况下，主线程会等待子线程结束后在结束
    3.同一个进程的线程间，数据共享
    4.多线程操作共享数据，可能会出现安全问题，可以用互斥锁解决

"""
import threading,time

def work():
    for i in range(5):
        time.sleep(0.2)
        print('working~~~~~')

if __name__ == '__main__':
    # 写法1：daemon属性
    # t = threading.Thread(target=work,daemon =True)
    # t.start()

    # setDaemon()函数，已经过时，但是还能用，以后的新版本可能会被移除掉
    # t = threading.Thread(target=work)
    # t.start()
    # t.setDaemon(True)

    # daemon属性
    t = threading.Thread(target=work)
    t.daemon = True
    t.start()

    time.sleep(1)
    print('主线程结束了')