#定义一个时钟类
import time

class Clock(object):
    def __init__(self,hour=0,minute=0,second=0):
        """

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self.hour =  hour
        self.minute = minute
        self.second = second

    def run(self):
        #时钟走动
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute ==60:
                self.minute = 0
                self.hour += 1
                if self.hour ==24:
                    self.hour = 0

    def show(self):
        return ('%d:%d:%d'% \
                (self.hour,self.minute,self.second))

def main():
    clock = Clock(23,59,58)
    while True:
        clock.run()
        time.sleep(1)
        print(clock.show())


if __name__ == '__main__':
    main()
