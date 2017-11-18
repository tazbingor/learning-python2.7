#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/17 下午8:33
# @Author  : Aries
# @Site    : 
# @File    : py035_dict.py
# @Software: PyCharm
'''
字典

'''

# 创建字典,以及字典赋值
# 1. 类似于列表和元组的赋值方式(集合)
mydict = {}
mydict = {2, 4, 6, 8}
print mydict  # set([8, 2, 4, 6])
print type(mydict)  # <type 'set'>
print '-' * 50

# 2. 字典一般赋值,采取键值对的方式
mydict = {
    2: 'two',
    4: 'four',
    6: 'six',
    8: 'eight'
}
print mydict  # {8: 'eight', 2: 'two', 4: 'four', 6: 'six'}
print type(mydict)  # <type 'dict'>
print '-' * 50

# 3. 使用内建函数dict()创建字典
myDict = dict({2: 'two',
               4: 'four',
               6: 'six',
               8: 'eight'})
print myDict
print type(myDict)  # <type 'dict'>
print '-' * 50

# 4.使用内建函数fromkeys()创建字典
myDict = {}.fromkeys((1, 2, 3, 4, 5), '1')
print myDict  # {1: '1', 2: '1', 3: '1', 4: '1', 5: '1'}
print type(myDict)  # <type 'dict'>
