# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import Spider
from tutorial.items import TutorialItem
from scrapy.selector import Selector

class DmozSpider(scrapy.Spider):
    # 爬虫名称
    name = "tutorial"
    # 设置下载延时
    download_delay = 1
    # 允许域名
    allowed_domains = ["doc.scrapy.org"]
    # 开始URL
    start_urls = [
        "http://doc.scrapy.org/en/latest/_static/selectors-sample1.html"
    ]

    def parse(self, response):
        #for sel in response.xpath('//html'):
        sel = Selector(response)
        for scope in sel.xpath('//div[@id="images"]/a'):
            item = TutorialItem()
            # 当前URL
            title = scope.xpath('@href').extract()#.decode('utf-8')
            item['title'] = title
            
            #author = response.selector.xpath('//div[@id="images"]/a/text()').extract()#.decode('utf-8')
            #item['author'] = author
            
            #releasedate = response.selector.xpath('//div[@id="images"]/a/img/@src').extract()#.decode('utf-8')
            #item['releasedate'] = releasedate
            yield item