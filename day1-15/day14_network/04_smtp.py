#使用python发送邮件

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    sender = '2891161929@qq.com'
    receivers = ['2891161929@qq.com', '439578717@qq.com']
    message = MIMEText('用python发送邮件的示例代码','plain','utf-8')
    message['From'] = Header('王大锤','utf-8')
    message['To'] = Header('郑仁伟','utf-8')
    message['Subject'] = Header('示例代码实验邮件','utf-8')
    smtper = SMTP('smtp.qq.com')

    smtper.login(sender,'123456')
    smtper.sendmail(sender,receivers,message.as_string())
    print('邮件发送完成')

if __name__ == '__main__':
    main()