"""
寻找所有水仙花数

Version: 1.0
Author: 郑仁伟
Date: 2020-02-04
"""

for num in range(100,1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)