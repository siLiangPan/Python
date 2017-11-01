#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter
import os

path="E:\\"
'''
list_dir=os.listdir(path)
print(list_dir)
'''
    
#os.chdir(path)
# 返回当前工作目录
str_b=os.getcwd()

list_dir=os.listdir(str_b)
print(list_dir)

# nt win7
print(os.name)