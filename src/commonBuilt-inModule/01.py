#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431937554888869fb52b812243dda6103214cd61d0c2000

'''
from datetime import datetime

# 获取当前日期和时间
now = datetime.now() # 获取当前datetime
print(now)
print(now.timestamp())
print(type(now))

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)
print(dt.timestamp()) # 把datetime转换为timestamp
# 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。


# timestamp转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t)) # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间 格林威治标准时间

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59.1', '%Y-%m-%d %H:%M:%S.%f')
print(cday)
'''
# datetime加减
from datetime import datetime, timedelta
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

# 本地时间转换为UTC时间
# 时区转换
