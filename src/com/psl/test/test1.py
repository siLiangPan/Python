#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('I\'m learning\nPython.')

print('''line1
... line2
... line3''')


a = 'ABC'
b = a
a = 'XYZ'
print(b)


n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print('n= ',n)
print('f= ',f)
print('s1= ',s1)
print('s2= ',s2)
print('s3= ',s3)
print('s4= ',s4)

# 在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
'''
常见的占位符
%d    整数
%f    浮点数
%s    字符串
%x    十六进制整数
'''
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

s1 = 72
s2 = 85
r = (85-72)*100/72
print('%02.1f%%' % r)
