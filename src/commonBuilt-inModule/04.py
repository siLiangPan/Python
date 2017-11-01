#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct
# pack函数把任意数据类型变成bytes
a=struct.pack('>I', 10240099)
print(a)

# unpack把bytes变成相应的数据类型：
b=struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(b)

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
p_a=struct.unpack('<ccIIIIIIHH', s)
print(p_a)
'''
两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
一个4字节整数：表示位图大小；
一个4字节整数：保留位，始终为0；
一个4字节整数：实际图像的偏移量；
一个4字节整数：Header的字节数；
一个4字节整数：图像宽度；
一个4字节整数：图像高度；
一个2字节整数：始终为1；
一个2字节整数：颜色数。
(b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
结果显示，b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24。
'''