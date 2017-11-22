#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 上午11:24
# @Author  : Aries
# @Site    : 
# @File    : py046_dict_iter.py
# @Software: PyCharm
'''
字典迭代
'''
legends = {
    ('Poe', 'author'): (1809, 1849, 1976),
    ('Gaudi', 'architect'): (1852, 1906, 1987),
    ('Freud', 'psychoanalyst'): (1856, 1939, 1990)
}

for eachLegend in legends:
    print eachLegend
    print legends[eachLegend]
print '-' * 50

# 字典迭代函数
# iteritems()
for i in legends.iteritems():
    print i
print '-' * 50

# iterkeys()
for i in legends.iterkeys():
    print i
print '-' * 50

# itervalues()
for i in legends.itervalues():
    print i
