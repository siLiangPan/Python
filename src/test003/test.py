#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
import keyword
print(keyword.kwlist)
'''
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue'
, 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global'
, 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise'
, 'return', 'try', 'while', 'with', 'yield']
'''

import math
print(math.pi)
print(math.e)


import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
'''
命令行参数为:
.\test.py
1
2
3
a
b
c

 python 路径为 
['E:\\workspace_psl\\IDE\\Python\\src\\test003',
 'E:\\workspace_psl\\IDE\\Python\\src',
 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python35\\DLLs',
 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python35\\lib',
 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python35',
 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python35\\lib\\site-packages',
 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python35\\python35.zip']
'''

