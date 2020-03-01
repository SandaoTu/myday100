#使用多线程

import random
from time import time, sleep
from threading import Thread

def download_task(filename):
    print('正在下载%s'%filename)
    time_to_download = random.randint(5,10)
    sleep(time_to_download)
    print('%s下载完成,共计耗时%s'%(filename,time_to_download))

def main():
    start_time = time()
    process1 = Thread(target=download_task,args=('python从入门到放弃',))
    process1.start()
    process2 = Thread(target=download_task,args=('喜剧之王.avi',))
    process2.start()
    process1.join()
    process2.join()
    end_time = time()
    print('总共耗时%.2f'%(end_time-start_time))

if __name__ == '__main__':
    main()