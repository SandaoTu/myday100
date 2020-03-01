"""
将一个正整数发转

Version: 1.0
Author: 郑仁伟
Date: 2020-02-04
"""

num = int(input('请输入一个需要反转的正整数： '))
reversed_num = 0
while num>0:
    reversed_num = reversed_num*10 + num % 10
    num //=10

print('发转后的正整数:',reversed_num)
