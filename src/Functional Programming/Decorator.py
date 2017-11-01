#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')
    
    
now()

import functools

def log(text):
    def decorator(func):
        # 把原始函数的__name__等属性复制到wrapper()函数中
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper   
    return decorator

@log('execute')
def now():
    print('2015-3-25')


now()    
print(now.__name__) 