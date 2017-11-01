#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
'''
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
'''


# 练习
import hashlib
db = {}
def register(username, password):
    md5 = hashlib.md5()
    string=password + username + 'the-Salt'
    md5.update(string.encode('utf-8'))
    get_mad5 = md5.hexdigest()
    #db['username'] = username
    db[username] = get_mad5
    print(db)
    
def login(username, password):
    md5 = hashlib.md5()
    string=password + username + 'the-Salt'
    md5.update(string.encode('utf-8'))
    md5_password = md5.hexdigest()
    if db[username] == md5_password:
        print('用户成功登陆...')
    else:
        print('账户或密码不正确！')
        
    
if __name__ == '__main__':
    register('michael','123456')
    login('michael','123456')
    