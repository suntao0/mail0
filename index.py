#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart # 引入内容扩展库
from email.header import Header


sender = '123@163.com' # 发件人

receivers = ['456@163.com', '789@163.com']  # 收件人


message = MIMEMultipart() # 创建带附件的实例
message['From'] = Header("主题，发件人", 'utf-8')
message['To'] =  Header("主题，收件人", 'utf-8')
message['Subject'] = Header('正文', 'utf-8')


message.attach(MIMEText('附件邮件', 'plain', 'utf-8')) # 正文内容


att = MIMEText(open('附件.txt', 'rb').read(), 'base64', 'utf-8') # 构造附件
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="附件"'
message.attach(att)
try:
    smtpObj = smtplib.SMTP('localhost') # 实例化smtp对象
    smtpObj.sendmail(sender, receivers, message.as_string()) # 发送邮件
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("无法发送邮件")
