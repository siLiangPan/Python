#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import pymysql

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
#engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
engine = create_engine('mysql+pymysql://root:tdx@123@192.168.0.147:3357/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


'''
插入

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='4', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
'''


'''
查询
'''
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()

'''
type: <class '__main__.User'>
name: Bob
'''

