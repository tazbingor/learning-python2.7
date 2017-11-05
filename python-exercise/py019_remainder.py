#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/5 下午4:20
# @Author  : Aries
# @Site    : 
# @File    : py019_remainder.py
# @Software: PyCharm

'''
有多少个三位整数能被17整除?将之输出。
'''

arr = []
for item in range(100, 1000, 1):
    if item % 17 == 0:
        arr.append(item)
print arr
print '有%s个三位数能被17整除' % str(len(arr))
