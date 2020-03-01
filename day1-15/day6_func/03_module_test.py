"""
不同模块中调用相同名字的函数

Verison: 1.0
Author: 郑仁伟
Date: 2020-02-06
"""
from module1 import foo
foo()

from module2 import foo
foo()

from module1 import foo as f1
from module2 import foo as f2
f2()
f1()