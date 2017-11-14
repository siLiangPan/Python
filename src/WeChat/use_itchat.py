#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
This script is designed to be run from inside py2exe
# 微信网页端的相关接口包
pip install itchat
# python 定时服务包
pip install apscheduler
'''
# python E:\workspace_psl\IDE\Python\src\WeChat\use_itchat.py

import itchat, time
import datetime as dt
from apscheduler.schedulers.background import BackgroundScheduler
import random

greeList = ['快去睡觉别熬夜','好好找工作加油','注意身体多喝热水','想你了求自拍']

def tick():
    users = itchat.search_friends(name=u'倩兰')  # 找到微信号名称
    userName = users[0]['UserName']
    #meetDate = dt.date(2014,2,15)
    meetDate = dt.datetime.strftime('2015-02-15 00:00:00')
    now = dt.datetime.now()    # 现在的时间
    #nowDate = dt.date.today    # 今天的日期
    nowDate = dt.datetime.now()    # 今天的日期
    passDates = (nowDate - meetDate).days
    itchat.send(u'今天是我们认识第%天，%s,晚安' %(passDates,random.sample(greeList,1)[0]))
    nextTickTime = now + dt.timedelta(days=1)
    nextTickTime = nextTickTime.strftime("%Y-%m-%d 00:00:00")
    my_scheduler(nextTickTime)   # 设定一个新的定时任务，明天零点准时问候
    

def my_scheduler(runTime):
    scheduler = BackgroundScheduler() # 生成对象
    scheduler._real_add_job(tick, 'date', run_date=runTime) # 在指定的时间，只执行一次
    scheduler.start()
    
    
    
if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=True)  # 在命令行中展示二维码，默认展示的是图片二维码
    #itchat.auto_login(hotReload=True)  # 这个是方便调试用的，不用每一次跑程序都扫码
    now = dt.datetime.now()  # 获取当前时间
    nextTickTime = now + dt.timedelta(days=1)
    nextTickTime = nextTickTime.strftime("%Y-%m-%d 08:45:00")
    my_scheduler(nextTickTime)
    itchat.run()    # 跑微信服务
    