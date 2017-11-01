#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct, os

def checkBmp(path):
    with open(path,'rb') as f:
        s=f.read(30)
    info=struct.unpack('<ccIIIIIIHH',s)
    if info[0]==b'B' and info[1]==b'M':
        print('这是一个位图文件：文图大小：%s x %s  颜色数：%s' %(info[6],info[7],info[9]))
    else:
        print('这不是一个位图文件.')

if __name__ == '__main__':
    checkBmp('C:\\Users\\Administrator\\Desktop\\test.bmp')