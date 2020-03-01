"""
输入圆的的半径计算圆的面接和周长

Version: 1.0
Author: 郑仁伟
"""

import math

radius=float(input('请输入圆的半径: '))
perimeter=2*math.pi*radius
area=math.pi*radius*radius

print('周长：%.2f'%perimeter)
print('面积：%.2f'%area)