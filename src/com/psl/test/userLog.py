# -*- coding: UTF-8 -*- 
'''
Created on 2017年9月11日

@author: Administrator
'''
#!/usr/bin/env python
#!/usr/bin/env python3
#coding=utf-8
#import raw_input
from pip._vendor.distlib.compat import raw_input
import getpass
name = raw_input('请输入用户名：')
pwd = getpass.getpass('请输入密码：')
if name == "alex" and pwd == "cmd":
    print ("欢迎，alex！")
else:
    print ("用户名和密码错误")