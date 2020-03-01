"""
用户身份验证

Version: 1.0
Author: 郑仁伟
"""

username = input('请输入用户名：')
password = input('请输入用户密码：')
if username == 'admin' and password == '123456':
    print('登录成功')
else:
    print('身份验证失败')