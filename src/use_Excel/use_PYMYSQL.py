#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = "PSL"
 
import pymysql
import contextlib
#定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
#def mysql(host='192.168.0.147', port=3357, user='root', passwd='tdx@123', db='tls_his',charset='utf8'):
def mysql(host='192.168.2.143', port=3306, user='root', passwd='123456', db='tls_his',charset='utf8'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    # #游标设置为字典类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()

def create_excel(fileName,db_datas,colnames):
    import xlwt
    # 创建一个Workbook对象，这就相当于创建了一个Excel文件  
    book = xlwt.Workbook(encoding='utf-8', style_compression=0) 
    # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。  
    # 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表  
    sheet = book.add_sheet('aa', cell_overwrite_ok=True)    # 其中的aa是这张表的名字
    # 写入字段名
    for j in range(len(colnames)):
        sheet.write(0, j, colnames[j])
    for i in range(0,len(db_datas)):
        for j in range(len(colnames)):
            sheet.write(i+1, j, db_datas[i][colnames[j]])
    book.save(fileName)
    
# 执行sql
with mysql() as cursor:
    #print(cursor)
    sql_str = r'''
    '''
    # 简化导出为excel的sql语句
    with open('sql.txt', 'r') as f:
        sql_str=f.read()
    row_count = cursor.execute(sql_str)
    # cursor.execute("select * from user")
    # cursor.execute('select * from user where id = %s', ('1',))
    # cursor.execute('CALL db_util.p_get_load_sql(%s,%s,%s);', ('201701','201712','E:/temp_data/'))
    # cursor.callproc('db_util.p_get_load_sql', args=(201701, 201712, 'E:/temp_data/'))
    #row_count = cursor.callproc('db_util.p_get_load_sql', args=(201701, 201712, 'E:/temp_data/'))
    # cursor.fetchone()
    # cursor.fetchone()
    '''
    cursor.scroll(1,mode='relative') # 相对当前位置移动
    cursor.scroll(2,mode='absolute') # 相对绝对位置移动
    '''
    # 获取数据
    row_1 = cursor.fetchall()
    #print(row_count)
    #print(row_1)
    #print(cursor.description)
    # 获取列名
    data_dict=[]
    for field in cursor.description:
        data_dict.append(field[0])
    #print (data_dict)
    create_excel(r'db_test.xls',row_1,data_dict)
    print(r'执行完毕！')
    '''
    for rs in row_1:
        print(rs)
        #print(rs['load_in_sql'])
    '''