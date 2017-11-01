#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    # value属性则是自动赋给成员的int常量，默认从1开始计数。
    print(name, '=>', member, ',', member.value)

'''
Jan => Month.Jan , 1
Feb => Month.Feb , 2
Mar => Month.Mar , 3
Apr => Month.Apr , 4
May => Month.May , 5
Jun => Month.Jun , 6
Jul => Month.Jul , 7
Aug => Month.Aug , 8
Sep => Month.Sep , 9
Oct => Month.Oct , 10
Nov => Month.Nov , 11
Dec => Month.Dec , 12
'''

'''
ImportError: cannot import name 'Enum'

是因为测试用的代码文件名字也命名的enum.py,
import的时候看样子是先导入这个文件, 所以找不到Enum.
测试文件改成其他名字的就OK了
看来后面自己写文件的名字最好按照一定的规则命名,防止和默认的冲突
'''
    
    
    
from enum import Enum, unique
# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    
for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)
    
'''
Sun => Weekday.Sun , 0
Mon => Weekday.Mon , 1
Tue => Weekday.Tue , 2
Wed => Weekday.Wed , 3
Thu => Weekday.Thu , 4
Fri => Weekday.Fri , 5
Sat => Weekday.Sat , 6
'''    
print(Weekday(1))