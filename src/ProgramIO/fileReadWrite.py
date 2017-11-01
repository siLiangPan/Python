#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# **********
# 读文件
# **********
try:
    f = open('/path/to/file', 'r')
    # 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：
    print(f.read())
    f.read(1024)
finally:
    if f:
        f.close()
        
        
with open('/path/to/file', 'r') as f:
    print(f.read())
    f.read
    
            
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉


# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：    
f = open('/Users/michael/test.jpg', 'rb')    
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
'''


# **********
# 写文件
# **********
with open('E:/workspace_psl/tmp/20170926/test.txt', 'w') as f:
    f.write('Hello, world!')
    
    
                