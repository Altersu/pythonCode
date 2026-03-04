import threading,time
def coding(name,num):
    for i in range(1,num+1):
        time.sleep(0.1)
        print(f'{name}正在敲第{i}遍代码！')

def music(name,num):
    for i in range(1,num+1):
        time.sleep(0.1)
        print(f'{name}正在听第{i}遍音乐~~~~~~~~')

if __name__ == '__main__':

    t1= threading.Thread(target=coding,args=('李想',5))
    t2= threading.Thread(target=music,kwargs={'num':5,'name':'xiaoming'})
    t2.start()
    t1.start()