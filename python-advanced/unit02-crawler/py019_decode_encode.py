#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/20 上午9:56
# @Author  : Aries
# @Site    : 
# @File    : py019_decode_encode.py
# @Software: PyCharm
'''
抓取sohu主页

在爬取网页中有一个新需求,倘若出现GBK或者UTF-8的页面该如何抓取?
使用chardet包
'''
import urllib2
import chardet

html = urllib2.urlopen('https://www.sohu.com/').read()
# print html.read().decode('GBK').encode('utf-8')

mychar = chardet.detect(html)
code = mychar['encoding']
if code == 'utf-8' or code == 'UTF-8':
    out_html = html
elif code == 'gb2312' or code == 'GBK' or code == 'GB2312':
    out_html = html.decode('GB2312', 'ignore').encode('utf-8')
print html
