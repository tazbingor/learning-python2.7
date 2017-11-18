#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/18 下午10:35
# @Author  : Aries
# @Site    : 
# @File    : py040_dictionary_key.py
# @Software: PyCharm
'''
字典的键
'''
# 字典不允许一个键有多个值
# 当有键发生冲突,则取最近的value赋值
dict1 = {'foo': 789, 'foo': 'xyz'}
print dict1  # {'foo': 'xyz'}
print len(dict1)  # 1
print dict1['foo']  # xyz

