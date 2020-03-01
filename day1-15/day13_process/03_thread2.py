#使用多线程
import random
from time import time, sleep
from threading import Thread

class DownloadTask(Thread):
    def __init__(self,filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('%s正在下载...'%self._filename)
        time_to_download = random.randint(5,10)
        sleep(time_to_download)
        print('%s下载完成,共计耗时%s'%(self._filename,time_to_download))


def main():
    start_time = time()
    t1 = DownloadTask('python从入门到放弃')
    t1.start()
    t2 = DownloadTask('喜剧之王.avi')
    t2.start()
    t1.join()
    t2.join()
    end_time = time()
    print('总共耗时%.2f'%(end_time-start_time))

if __name__ == '__main__':
    main()