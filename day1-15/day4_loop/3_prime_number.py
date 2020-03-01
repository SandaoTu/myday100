"""
输入一个正整数判断是不是素数

Version :1.0
Author: 郑仁伟
Date: 2020-02-04
"""

number = int(input('请输入一个正整数：'))
is_prime = True

for  i in range(2,number):
    if number % i == 0:
        is_prime = False
        break
if is_prime == True :
    print('%d是一个素数'%number)
else:
    print('%d不是一个素数'%number)
