"""
在屏幕上显示跑马灯效果

"""
import os
import time

def main():
    str = ' Hello word....！'
    while True:
        #清空屏幕输入
        os.system('cls')
        print(str)
        time.sleep(0.2)
        str = str[1:]+str[0]

if __name__ == '__main__':
    main()