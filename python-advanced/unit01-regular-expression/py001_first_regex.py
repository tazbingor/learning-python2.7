#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/6 下午9:03
# @Author  : Aries
# @Site    : 
# @File    : py001_first_regex.py
# @Software: PyCharm
'''
第一个正则表达式

正则表达式的作用:校验字符串
'''
import re

if __name__ == '__main__':

    string = 'an example word:cat!'
    match = re.search(r'world:\w\w\w\w', string)
    if match:
        print 'found', match.group()
    else:
        print 'did not find'
