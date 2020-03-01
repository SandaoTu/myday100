#使用多线程方式，从网络上下载图片

import requests
from threading import Thread
from time import time

class DownloadHanlder(Thread):
    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/')+1:]
        resp = requests.get(self.url)
        with open('./res/'+filename,'wb') as f:
            f.write(resp.content)

def main():
    resp = requests.get('http://api.tianapi.com/meinv/index?key=f424b6b10d392569bec89576d2e64e7a&num=10')
    #将服务器返回的json数据解析成为字典
    data_model = resp.json()
    for m_dict in data_model['newslist']:
        url = m_dict['picUrl']
        #通过多线程实现图片下载
        DownloadHanlder(url).start()

if __name__ == '__main__':
    main()
