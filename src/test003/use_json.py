#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
import json

# Python 字典类型转换为 JSON 对象
data1 = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])

'''
import calendar
calendar.setfirstweekday(6)
a=calendar.calendar(2017,w=2,l=1,c=6)
print(a)
f = open('./2017.txt','w')
f.write(a)
f.close;

