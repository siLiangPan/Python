# -*- coding: UTF-8 -*-  
# How to write to an Excel using xlwt module  
import xlwt  
# 创建一个Workbook对象，这就相当于创建了一个Excel文件  
book = xlwt.Workbook(encoding='utf-8', style_compression=0)  
  
# 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。  
# 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表  
sheet = book.add_sheet('aa', cell_overwrite_ok=True)    # 其中的aa是这张表的名字  
  
# 向表aa中添加数据  
sheet.write(0, 0, 'EnglishName')    # 其中的'0, 0'指定表中的单元，'EnglishName'是向该单元写入的内容  
sheet.write(1, 0, 'Marcovaldo')  
txt1 = '中文名字'  
sheet.write(0, 1, txt1) # 此处需要将中文字符串解码成unicode码，否则会报错  
txt2 = '马可瓦多'  
sheet.write(1, 1, txt2)  
  
# 最后，将以上操作保存到指定的Excel文件中  
#book.save(r'e:\try1.xls') #在字符串前加r，声明为raw字符串，这样就不会处理其中的转义了。否则，可能会报错 
book.save(r'try1.xls')