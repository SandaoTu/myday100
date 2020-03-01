"""
百分制成绩转换程为等级制成绩

Version: 1.0
Author: 郑仁伟
"""

score = float(input('请输入得分：'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade =  'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应等级是：',grade)