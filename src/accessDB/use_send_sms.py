#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import urllib, urllib2, sys
import urllib.request, sys


host = 'http://sms.market.alicloudapi.com'
path = '/singleSendSms'
method = 'GET'
appcode = 'ffbe2ec700fe4bb1b6c6f5c4c5e528f5'
querys = 'ParamString=%7B%22no%22%3A%22123456%22%7D&RecNum=15102776421&SignName=%e6%bd%98%e6%80%9d%e4%ba%ae&TemplateCode=SMS_105380052'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content)