#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/19 下午7:02
# @Author  : Aries
# @Site    : 
# @File    : py014_urlopen_request.py
# @Software: PyCharm
'''
urllib2 的 urlopen() 和 Request()

防止反爬虫的手段: 明确指定消息头中User-Agent的信息
'''
import urllib2

# 指定User-Agent
user_agent_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

# 向指定url地址发送请求,并返回服务器响应的类文件对象
# response = urllib2.urlopen('http://www.baidu.com/')

# 或者 通过request重构一个请求对象
request = urllib2.Request('http://www.baidu.com/', headers=user_agent_headers)
response = urllib2.urlopen(request)
html = response.read()

print html
