#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
 ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
'''

import threading
import os

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
    # 获取进程名称
    print(os.getpid())

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

# 打印主线程名
print(threading.current_thread().name)
t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
# join()的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
t1.join()
t2.join()

