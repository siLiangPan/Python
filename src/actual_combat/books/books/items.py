# -*- coding: utf-8 -*-  
  
# Define here the models for your scraped items  
#  
# See documentation in:  
# http://doc.scrapy.org/en/latest/topics/items.html  
  
import scrapy  
  
  
class BooksItem(scrapy.Item):  
    book_name = scrapy.Field()      #图书名  
    book_star = scrapy.Field()      #图书评分  
    book_pl = scrapy.Field()        #图书评论数  
    book_author = scrapy.Field()    #图书作者  
    book_publish = scrapy.Field()   #出版社  
    book_date = scrapy.Field()      #出版日期  
    book_price = scrapy.Field()     #图书价格  
    

#item的操作和 dict API 非常相似。
'''    
booksItem = BooksItem(book_name='Desktop PC', book_price=1000)
print(booksItem)
# {'book_name': 'Desktop PC', 'book_price': 1000}
print(booksItem['book_name'])

'''