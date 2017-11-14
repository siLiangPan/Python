#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = "PSL"
 
import pymysql
import contextlib
#定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def mysql(host='192.168.0.147', port=3357, user='root', passwd='tdx@123', db='test',charset='utf8'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    # #游标设置为字典类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()

# 执行sql
with mysql() as cursor:
    #print(cursor)
    # cursor.execute("select * from user")
    # cursor.execute('select * from user where id = %s', ('1',))
    # cursor.execute('CALL db_util.p_get_load_sql(%s,%s,%s);', ('201701','201712','E:/temp_data/'))
    # cursor.callproc('db_util.p_get_load_sql', args=(201701, 201712, 'E:/temp_data/'))
    row_count = cursor.callproc('db_util.p_get_load_sql', args=(201701, 201712, 'E:/temp_data/'))
    # cursor.fetchone()
    # cursor.fetchone()
    '''
    cursor.scroll(1,mode='relative') # 相对当前位置移动
    cursor.scroll(2,mode='absolute') # 相对绝对位置移动
    '''
    row_1 = cursor.fetchall()
    #print(row_count, row_1)
    print(row_1)
    '''
    for rs in row_1:
        print(rs)
        #print(rs['load_in_sql'])
    '''