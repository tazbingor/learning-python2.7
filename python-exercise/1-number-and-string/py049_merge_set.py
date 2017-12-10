#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/19 下午6:20
# @Author  : Aries
# @Site    : 
# @File    : py049_merge_set.py
# @Software: PyCharm
'''
合并字典

哪些字典方法可以把两个字典合并到一起？

'''

# update()合并字典
dict1 = {'a', 'b', 'c'}
dict2 = {'d', 'e', 'f'}
dict1.update(dict2)
print dict1  # set(['a', 'c', 'b', 'e', 'd', 'f'])

