#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
# email负责构造邮件
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')

# smtplib负责发送邮件。
import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'pansiliang2007@126.com' #input('From: ')
password = 'psl15971279885' #input('Password: ')
to_addr = '425274873@qq.com' #input('To: ')
smtp_server = 'smtp.126.com' #input('SMTP server: ')
smtp_port = 25 # SMTP协议默认端口是25  587  465
# plain 纯文本文件
# html  HTML邮件
#msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg = MIMEMultipart()
'''
# 同时支持HTML和Plain格式
msg = MIMEMultipart('alternative')
'''
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
#msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
'''
# 发送HTML邮件
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8'))
# 图片嵌入到邮件正文中
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
'''

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
#with open('/Users/michael/Downloads/test.png', 'rb') as f:
with open('C:\\Users\\Administrator\\Desktop\\o_Logstash filter插件.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)


# 发送HTML邮件
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8'))

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls() # 创建SSL安全连接
server.set_debuglevel(1) # 可以打开或关闭调试信息
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()