#
# import time
# import threading
#
# def sing():
#     while True:
#         print("正在唱歌...")
#         time.sleep(1)
#
# def dance():
#     while True:
#         print("正在跳舞...")
#         time.sleep(1)
#
# if __name__ == '__main__':
#     sing_thread = threading.Thread(target=sing)
#     dance_thread = threading.Thread(target=dance)
#     sing_thread.start()
#     dance_thread.start()


import time
import threading

def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing,args=("singing~~~",))
    dance_thread = threading.Thread(target=dance,kwargs={"msg":"dancing~~~"})
    sing_thread.start()
    dance_thread.start()