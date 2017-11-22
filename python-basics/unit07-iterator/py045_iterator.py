#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/20 下午10:06
# @Author  : Aries
# @Site    : 
# @File    : py045_iterator.py
# @Software: PyCharm
'''
迭代器
'''
str_tuple = ('JS', 'py', 'class')
i = iter(str_tuple)
print i.next()  # JS
print i.next()  # py
print i.next()  # class

print '-' * 50

# 迭代器工作原理

fetch = iter(str_tuple)
while True:
    try:
        item = fetch.next()
    except StopIteration:
        break
    print item
print '-' * 50

