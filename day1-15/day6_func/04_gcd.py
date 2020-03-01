"""
求两个数的最大公约数和最小公倍数

Version: 1.0
Author: 郑仁伟
Date: 2020-02-06
"""
#求两个数的最大公约数
def gcd(x,y):
    if x>y:
        item=x
        x = y
        y=item
    gcd_num = 1
    for i in range(x,0,-1):
        if x%i == 0 and y%i == 0:
            gcd_num = i
        break
    return gcd_num

#求两个数的最小公约数
def lcm(x,y):
    return x*y/gcd(x,y)

if __name__ == '__main__':
    num1 = int(input('请输入数字1：'))
    num2 = int(input('请输入数字2：'))
    print('%d和%d的最大公约数为：%d'%(num1,num2,gcd(num1,num2)))
    print('%d和%d的最小公倍数为：%d'%(num1,num2,lcm(num1,num2)))