#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import hashlib
import time
import os


import math

class VectorCompare:
    #计算矢量大小
    def magnitude(self,concordance):
        total = 0
        for word,count in concordance.items():
            total += count ** 2
        return math.sqrt(total)
    #计算矢量之间的 cos 值
    def relation(self,concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            '''
            # Python3以后删除了has_key()方法！
            if adict.has_key(key1):   改为
            if key1 in adict:
            '''
            #if concordance2.has_key(word):
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


#将图片转换为矢量
def buildvector(im):
    d1 = {}

    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1

v = VectorCompare()

#图标集合
iconset = ['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#加载训练集
imageset = []  # list

for letter in iconset:
    for img in os.listdir('./iconset/%s/'%(letter)):
        temp = []
        if img != "Thumbs.db" and img != ".DS_Store": # windows check...
            #将图片转换为矢量，并加入temp列表
            temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
        # 字典加入imageset列表
        imageset.append({letter:temp})


#im = Image.open("captcha.gif")
im = Image.open("./examples/xfnrsn.gif")
im2 = Image.new("P",im.size,255)
#(将图片转换为8位像素模式)
im.convert("P")
#打印颜色直方图
#print im.histogram()
temp = {}  # 字典

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))  # 获取每个坐标像素点的RGB值
        temp[pix] = pix
        if pix == 220 or pix == 227: # these are the numbers to get
            im2.putpixel((y,x),0)
'''
提取单个字符图片
'''
inletter = False
foundletter=False
start = 0
end = 0

letters = []

for y in range(im2.size[0]): # slice across
    for x in range(im2.size[1]): # slice down
        pix = im2.getpixel((y,x)) # 获取每个坐标像素点的RGB值
        if pix != 255:
            inletter = True

    if foundletter == False and inletter == True:
        foundletter = True
        start = y

    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start,end))  # tuple 添加到 list


    inletter=False
###############################
'''
得到每个字符开始和结束的列序号
'''
count = 0
result = []
#对验证码图片进行切割
for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))

    guess = []
    #将切割得到的验证码小片段与每个训练片段进行比较
    for image in imageset:
        #for x,y in image.iteritems():    # image.iteritems()返回的是一个生成器(迭代器)
        # Python3.5中：iteritems变为items
        for x,y in image.items():
            if len(y) != 0:
                # 计算矢量之间的 cos 值 |  将图片转换为矢量
                guess.append( ( v.relation(y[0],buildvector(im3)),x) )

    guess.sort(reverse=True)
    print ("",guess[0][0],guess[0][1])
    result.append(guess[0][1])
    count += 1
    
print(''.join(result))