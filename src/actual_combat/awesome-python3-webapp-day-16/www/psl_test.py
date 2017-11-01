#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from orm import create_pool
import orm
import asyncio

__pool={}
def test():
    global __pool
    print(__pool)
    orm.create_pool(loop=1,user='root',password='tdx@123',db='test')
    print(__pool)
    sql='CALL db_util.p_get_load_sql(?,?,?);'
    args=(201701, 201712, 'E:/temp_data/')
    row_1 = orm.select(sql,args)
    for rs in row_1:
        print(rs['load_in_sql'])


test()


'''
import pymysql
# 获取数据源
def create_pool():
    conn = pymysql.connect(host='192.168.0.147', port=3357, user='root', passwd='tdx@123', db='test',charset='utf8')
    return conn
  
conn=create_pool()
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
row_count = cursor.callproc('db_util.p_get_load_sql', args=(201701, 201712, 'E:/temp_data/'))
row_1 = cursor.fetchall()
for rs in row_1:
    print(rs['load_in_sql'])
conn.commit()
cursor.close()
conn.close()
'''