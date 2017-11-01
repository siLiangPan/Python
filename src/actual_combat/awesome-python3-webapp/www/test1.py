#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'psl'  #作者
__date__ = "2017/10/23 10:24"  #创建时间

import orm
import asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop,user='www-data', password='www-data', db='awesome')

    u = User(name='Test', email='test2@example.com', passwd='1234567890', image='about:blank')

    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
'''
for x in test():
    pass
'''