#不使用多进程

import random
from time import time ,sleep

def download_task(filename):
    print('%s正在下载'%filename)
    time_to_download = random.randint(5,10)
    sleep(time_to_download)
    print('%s下载完成，共耗时%s秒'%(filename,time_to_download))

def main():
    start_time = time()
    download_task('python从入门到放弃.pdf')
    download_task('喜剧之王.avi')
    end_time = time()
    print('总共耗时%.2f秒'%(end_time-start_time))

if __name__ == '__main__':
    main()