#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/16 下午7:48
# @Author  : Aries
# @Site    : 
# @File    : py013_first_crawler.py
# @Software: PyCharm
'''
使用的urllib2爬虫的第一行代码
'''
import urllib2

response = urllib2.urlopen('https://www.bilibili.com/')
html = response.read()
print html  # 输出为B站的源码
