"""
字典的使用

"""
#创建字典的字面量语法
score = {'郑仁伟':'99','刘德华':'89','郭富城':'88'}
print(score)

#创建字典的构造器语法
item1 = dict(one=1,tow=2,three=3)
print(item1)

#通过zip函数将两个序列压成字典
item2 = dict(zip(['a','b','c'],'123'))
print(item2)

#创建字典的推导式语法
item3 = {'n{}'.format(num):num**2 for num in range(5)}
print(item3)

# 清除字典
score.clear()
print(score)