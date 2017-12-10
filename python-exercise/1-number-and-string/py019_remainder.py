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

count = 1  # 计数器
item = 0
while item < 1001:
    if item % 17 == 0:
        print item
        count += 1
    item += 1
print '有%s个三位数可以被17整除' % str(count)
