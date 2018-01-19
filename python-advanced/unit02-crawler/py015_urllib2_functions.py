#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/19 下午8:00
# @Author  : Aries
# @Site    : 
# @File    : py015_urllib2_functions.py
# @Software: PyCharm
'''
urllib2 常用内建函数

# 返回响应码,成功则返回200,4开头页面异常,5开头服务器异常
response.getcode()

# 返回实际数据的URL,防止重定向的问题
response.geturl()

# 返回服务器响应的http消息头
response.info()
'''
import urllib2

# 指定User-Agent
user_agent_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

# 或者 通过request重构一个请求对象
request = urllib2.Request('http://www.baidu.com/', headers=user_agent_headers)
response = urllib2.urlopen(request)

# 返回响应码,成功则返回200,4开头页面异常,5开头服务器异常
print response.getcode()  # 200

# 返回实际数据的URL,防止重定向的问题
print response.geturl()  # https://www.baidu.com/

# 返回服务器响应的http消息头
print response.info()
