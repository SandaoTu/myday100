"""
自动求和

Version：1.0
Author:zrw
Date: 2020-02-05
"""

num_start = int(input('请输入起始数字：'))
num_stop = int(input('请输入结束数字： '))
num = 0
for i in range(num_start,num_stop+1):
    print('num%d=%d+%d' % (i,num, i))
    num = num + i

print(num)
