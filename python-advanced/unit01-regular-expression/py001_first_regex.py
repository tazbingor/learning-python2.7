#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/6 下午9:03
# @Author  : Aries
# @Site    : 
# @File    : py001_first_regex.py
# @Software: PyCharm
'''
第一个正则表达式
'''
import re

str = 'an example word:cat!'
match = re.search(r'world:\w\w\w\w', str)
if match:
    print 'found', match.group()
else:
    print 'did not find'
