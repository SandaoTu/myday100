"""
设计一个函数产生指定长度的验证码，验证码由数字和大小写字母构成

Version: 1.0
Author: 郑仁伟
Date: 2020-02-06
"""
from random import randint

def generate_code(code_len=4):
    all_char = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMANOPQRSTUVWXYZ'
    last_pos = len(all_char)
    code = ''
    for _ in range(code_len):
        index = randint(0,last_pos)
        code += all_char[index]
    return code

if __name__ == '__main__':
   print(generate_code())
   print(generate_code(10))
