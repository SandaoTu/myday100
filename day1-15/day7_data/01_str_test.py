#使用*运算符来重复一个字符串
s1='Hello, world'*3
s2 = "Hello,world"
s3 = """
HELLO,
WORLD
"""
print(s1)
print(s3)

#转义字符 反斜杠\
s4 = '\'hellworld\''
print(s4)
print('nihao\nwoyehao\tdajiahao')

s5 = 'abc12345678'
#切片运算,[]和[:]从字符串中提取某些字符
print(s5[2])
print(s5[2:6])
print(s5[::-1])