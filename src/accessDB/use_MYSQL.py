#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Python中操作mysql的pymysql模块详解
http://www.cnblogs.com/wt11/p/6141225.html

MySQL-Connector-Python
这个模块和上面c编写的就截然不同了，这个模块完全由纯python编写，血统纯正，也就是由此会比上面的三个模块慢，
但是这个模块有个好爸爸，是由oracle所持有，而且傲娇的oracle没有把这个模块放到pypi，所以你懂得，安装要自己下载。
当然了这个模块是支持python3，而且也比较稳定，毕竟是大厂出品，用起来体验很不错。

PyMySQL
这个模块是作者积极推荐的模块，社区活跃，开源，支持pypi，由纯python编写，支持所有的Openstack标准，
应该是py里现在最火的数据库连接模块了，而且可以在Django中替代MySqldb，用起来很不错。
'''
'''
安装MySQL驱动
由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。
MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：
$ pip install mysql-connector-python --allow-external mysql-connector-python
$ pip install mysql-connector-python

如果上面的命令安装失败，可以试试另一个驱动：
$ pip install PyMySQL
$ pip install mysql-connector
通过pip安装SQLAlchemy：  # ORM技术：Object-Relational Mapping
pip install sqlalchemy
'''

# 导入MySQL驱动:
#import mysql.connector
import pymysql
# 创建连接
conn = pymysql.connect(host='192.168.0.147', port=3357, user='root', passwd='tdx@123', db='test', charset='utf8')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount) # 1
# 执行SQL，并返回受影响行数,执行多次
#effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
'''
# 获取剩余结果的第一行数据
row_1 = cursor.fetchone()
# 获取剩余结果前n行数据
# row_2 = cursor.fetchmany(3)
# 获取剩余结果所有数据
# row_3 = cursor.fetchall()
'''
print(values)
'''
(('1', 'Michael'),)

'''
# 关闭Cursor和Connection:
cursor.close()
conn.close()

