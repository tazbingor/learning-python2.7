#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/2 下午4:31
# @Author  : Aries
# @Site    : 
# @File    : py017_bitwise.py
# @Software: PyCharm

'''
位运算符
'''

# ~ 取反
print ~1  # -2
print ~ -1  # 0
print ~0  # -1

# & 按位与
print 100 & 50  # 32
print 2 & 1  # 0
print 9 & 3  # 1

# | 或
print 100 | 50  # 118
print 1 | 1  # 1
print 10 | 2  # 10

# ^ 抑或
print 100 ^ 50  # 86
print 10 ^ 2  # 8

# << 左移
print 10 << 2  # 40
print 100 << 1  # 200

# >> 右移
print 10 >> 2  # 2
print 100 >> 1  # 50
