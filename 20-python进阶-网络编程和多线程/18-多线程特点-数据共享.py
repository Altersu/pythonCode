
import threading,time

my_list= []

def write_data():
    for i in range(1,6):
        my_list.append(i)
        print(f'添加数据：{i}')
    print(f'write_data函数：{my_list}')

def read_data():
    time.sleep(1)
    print(f'read_data函数：{my_list}')

if __name__ == '__main__':
    t1 = threading.Thread(target=write_data)
    t2 = threading.Thread(target=read_data)

    t1.start()
    t2.start()