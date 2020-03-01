#进程之间进行通信,下面程序有问题
#程序在创建进程的时候，子进程会赋值父进程及其所有的数据结构，每个子进程有自己独立的内存空间
#这也意味着两个子进程中各拥有一个counter，所有结果可想而知
#可以使用multiprocessing模块中的Queue类，它是可以被多个进程共享得队列

from multiprocessing import Process
from time import sleep

counter = 0

def sub_task(string):
    global counter
    while counter<10:
        print(string,end='',flush=True)
        counter += 1
        sleep(0.01)

def main():
    Process(target=sub_task,args=('Ping',)).start()
    Process(target=sub_task,args=('Pong',)).start()

if __name__ == '__main__':
    main()