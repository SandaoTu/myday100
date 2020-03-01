"""
猜数字游戏
计算机给出一个从1~100的随机数
计算机根据人给出的数字分别提示大一点/小一点/猜对了

Versoin:  1.0
Author: 郑仁伟
"""

import random

answer = random.randint(1,100)
couter=0
while True:
    couter += 1
    number = int(input('请输入： '))
    if number > answer:
        print('猜小一点')
    elif number <answer:
        print('猜大一点')
    else:
        print('猜对了！')
        break
print("您一共猜了%d次"%couter)
if couter > 7:
    print('您的智商有点堪忧哦！再试试吧！')
else:
    print("你真是个小天才呢！")