"""
函数重载例子

Version: 1.0
Author: 郑仁伟
Date: 2020-02-06
"""
from random import randint

def roll_dice(n=2):
    """摇骰子"""
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

def add(a=0, b=0, c=0):
    return a+b+c

#在参数名前面的*表示args是一个可变参数
def add2(*args):
    total=0
    for val in args:
        total += val
    return total

print(roll_dice())
print(roll_dice(5))

print(add())
print(add(1))
print(add(1,2,))
print(add(1,2,3))

print(add2())
print(add2(2,3,4,5))