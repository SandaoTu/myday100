"""
输入年份判断是否是闰年

Version: 1.0
Author: 郑仁伟
"""

year = int(input('请输入年份： '))
is_leap = (year%4 == 0 and year%100 != 0) \
          or year%400 == 0

print( '闰年' if is_leap else '不是闰年')