#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

im = Image.open('test.png')
# im.show() # 系统打开图片
print(im.format, im.size, im.mode)
im = im.convert('RGB')  # 解决 OSError: cannot write mode RGBA as JPEG
# PNG (400, 300) RGB
# PNG (1093, 634) RGBA

im.thumbnail((800, 800))
im.save('thumb.jpg', 'JPEG')
im2 = Image.open('thumb.jpg')
im2.show() # 系统打开图片