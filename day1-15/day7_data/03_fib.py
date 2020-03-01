"""
斐波拉契数列
使用yield关键字将一个普通函数改造成生成器函数

Version: 1.0
Author: 郑仁伟
Date: 2020-02-06
"""

def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, (a+b)
        yield a

def main():
    for val in fib(5):
        print(val)

if __name__ == '__main__':
    main()