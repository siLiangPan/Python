#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = "PSL"
 
import pymysql
import contextlib
#定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
#def mysql(host='192.168.0.147', port=3357, user='root', passwd='tdx@123', db='tls_his',charset='utf8'):
def mysql(host='192.168.2.143', port=3306, user='root', passwd='123456', db='tls_his',charset='utf8'):
#def mysql(host='192.168.2.142', port=3306, user='root', passwd='123456', db='tls_cluster',charset='utf8'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
    # #游标设置为字典类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()
        conn.close()

def write_excel(sheet,line,db_row,style,db_datas,colnames,location_dict):
    
    sheet.write(line, 0, db_row['host_name'])  # 第line行，第1列
    sheet.write(line, 1, db_row['location'])   # 第line行，第2列
    sheet.write(line, 2, db_row['time_quantum'])   # 第line行，第2列\
    sheet.write(line, 3, db_row['days'])   # 第line行，第2列
    sheet.write(line, 4, db_row['login_days'])   # 第line行，第2列
    
    '''
    # 写入字段名
    for j in range(len(colnames)):
        sheet.write(0, j, colnames[j])  # 第1行，第j列
    '''
    pattern = Pattern()                 # 创建一个模式                                        
    pattern.pattern = Pattern.SOLID_PATTERN     # 设置其模式为实型   
    #pattern.pattern_fore_colour = 1 # 初始化为白色
    # 设置单元格背景颜色 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta,  the list goes on...
                    
                
    for i in range(0,len(db_datas)):
        #print(db_row['host_name'] + "-" + db_row['location'])
        #print(db_datas[i][colnames[0]] + "-" + db_row['min_day'] + "-" + db_row['max_day'])
        for j in range(len(colnames)):
            if j == 0:
                sheet.write(0, i+5, db_datas[i][colnames[j]])
            elif j == 1:
                if int(db_datas[i]['day']) >= int(db_row['min_day']) and int(db_datas[i]['day']) <= int(db_row['max_day']):
                    #pattern.pattern_fore_colour = line+1
                    pattern.pattern_fore_colour = location_dict[db_row['location'].split()[0]]
                    style.pattern = pattern             # 将赋值好的模式参数导入Style
                    sheet.write(line, i+5, db_datas[i][colnames[j]],style)   
                    sheet.write(line, 1, db_row['location'],style)   # 第line行，第2列                 
                else:
                    sheet.write(line, i+5, db_datas[i][colnames[j]])

   
    
host_names = ["0WQO1ZHDXRPEIFM","0WQO1ZHDXRPEIFM","0WQO1ZHDXRPEIFM","23GND9SHIQQUNIQ","23GND9SHIQQUNIQ","23GND9SHIQQUNIQ","23GND9SHIQQUNIQ","AALB-NNRKSK","CW033","D992HUI","D992HUI","D992HUI","DESKTOP-DB8U28F","DESKTOP-LC148N4","DESKTOP-O5BHC24","HGTJ-2QXX99","HGTJ-2QXX99","HGTJ-2QXX99","IWVTALWYV6W2N0E","IWVTALWYV6W2N0E","JWHR-TRUHXO","LAPTOP-0C69P3IL","LS--20160731VJA","LS--20160731VJA","LS--20160731VJA","LS--20160731VJA","LS--20160731VJA","LS--20160731VJA","LS--20160731VJA","MICROSOF-64885F","O4EXJOGTZ6WFUNL","PC-20170115QOOO","RCEJ-43BKWW","RCEJ-43BKWW","RCEJ-43BKWW","USER-20160621HU","VGTG-WXVJ8V","VGTG-WXVJ8V","VGTG-WXVJ8V","WIN-01702061424","WIN-0NCUACU0TSB","WWHU-8ZX16Q","WWHU-8ZX16Q","WWHU-8ZX16Q","WWHU-8ZX16Q","WWHU-8ZX16Q","WWHU-8ZX16Q","WWHU-8ZX16Q","WWW-7374312DB85","XPQA-SXU90E","XPQA-SXU90E","XPQA-SXU90E","XPQA-SXU90E","XPQA-SXU90E","XPQA-SXU90E"]
locations = ["江苏省扬州市 电信","江西省景德镇市 电信","福建省厦门市 联通","广东省佛山市 电信","江苏省镇江市 电信","浙江省绍兴市 电信","福建省厦门市 联通","北京市北京市 联通","江苏省无锡市 电信","北京市石景山区","福建省厦门市 联通","贵州省黔西南布依族苗族自治州兴义市 电信","北京市北京市 联通","上海市上海市 移动","上海市上海市 移动","安徽省淮南市 电信","浙江省杭州市 联通","福建省厦门市 联通","江苏省扬州市 电信","福建省厦门市 联通","浙江省杭州市 联通","广东省广州市 电信","四川省眉山市仁寿县 电信","江苏省扬州市 电信","江苏省淮安市 联通","浙江省嘉兴市 联通","甘肃省兰州市 联通","福建省厦门市 电信","福建省厦门市 联通","陕西省西安市灞桥区 电信","浙江省温州市 电信","陕西省西安市 电信","江苏省苏州市 电信","福建省厦门市 联通","福建省泉州市 电信","浙江省温州市 电信","北京市北京市 联通","江西省宜春市 电信","福建省厦门市 联通","福建省厦门市 联通","福建省厦门市 联通","上海市上海市 电信","上海市浦东新区 联通","安徽省合肥市 电信","广东省深圳市 电信","浙江省杭州市 电信","福建省厦门市 联通","福建省福州市 电信","陕西省西安市 电信","上海市上海市 联通","安徽省淮南市 电信","江苏省宿迁市 电信","浙江省杭州市 华数","福建省厦门市 联通","福建省福州市 电信"]    
location_dict = {'上海市上海市':2,'上海市浦东新区':3,'北京市北京市':4,'北京市石景山区':5,'四川省眉山市仁寿县':6,'安徽省合肥市':7,'安徽省淮南市':51,'广东省佛山市':52,'广东省广州市':10,'广东省深圳市':11,'江苏省宿迁市':12,'江苏省扬州市':13,'江苏省无锡市':14,'江苏省淮安市':15,'江苏省苏州市':16,'江苏省镇江市':17,'江西省宜春市':18,'江西省景德镇市':19,'浙江省嘉兴市':20,'浙江省杭州市':21,'浙江省温州市':22,'浙江省绍兴市':23,'甘肃省兰州市':24,'福建省厦门市':25,'福建省泉州市':26,'福建省福州市':27,'贵州省黔西南布依族苗族自治州兴义市':28,'陕西省西安市':29,'陕西省西安市灞桥区':30}

# 执行sql
with mysql() as cursor:
    
    sql_str = r'''
    '''
    # 简化导出为excel的sql语句
    with open('sql.txt', 'r', encoding='utf-8') as f:
        sql_str=f.read()
    row_count = cursor.execute(sql_str)
    # 获取数据
    row_lp1 = cursor.fetchall()
        
    import xlwt
    from xlwt import XFStyle,Pattern
    # 创建一个Workbook对象，这就相当于创建了一个Excel文件  
    book = xlwt.Workbook(encoding='utf-8', style_compression=0) 
    # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。  
    # 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表  
    sheet = book.add_sheet('aa', cell_overwrite_ok=True)    # 其中的aa是这张表的名字
    style = XFStyle()                       #赋值style为XFStyle()，初始化样式
    fileName=r'db_test.xls'
    
    #for i in range(len(host_names)):
    i = 0
    for ts in row_lp1:
    #row_count = cursor.execute(sql_str)
    # cursor.execute("select * from user")
    # cursor.execute('select * from user where id = %s', ('1',))
    # cursor.execute('CALL db_util.p_get_load_sql(%s,%s,%s);', ('201701','201712','E:/temp_data/'))
    # cursor.callproc('db_util.p_get_load_sql', args=(201701, 201712, 'E:/temp_data/'))
        #row_count = cursor.callproc('tls_his.p_tmp_get_data_20180123', args=(host_names[i], locations[i]))
        row_count = cursor.callproc('tls_his.p_tmp_get_data_20180123', args=(ts['host_name'], ts['location']))
        # 获取数据
        row_1 = cursor.fetchall()
        # 获取列名
        data_dict=[]
        for field in cursor.description:
            data_dict.append(field[0])
            #print (data_dict)
        write_excel(sheet,i+1,ts,style,row_1,data_dict,location_dict)
        i += 1
        
    book.save(fileName)
    print(r'执行完毕！')
        