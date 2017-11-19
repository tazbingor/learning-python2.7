#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/19 下午5:09
# @Author  : Aries
# @Site    : 
# @File    : py043_aggregate_operator.py
# @Software: PyCharm
'''
集合操作符
'''

# 1.集合,等价和不等价
s = set('python')
t = frozenset('python')
print s == t  # True
print s != t  # False
print s is t  # False
print '-' * 50

# 2.子集和超集
s1 = set('py')
print s1 < s  # True
print s1 < t  # True
print '-' * 50

# 3.联合 union 两个或者多个集合联合成一个新集合
s2 = set('Java')
s3 = set('Script')
print s2 | s3  # set(['a', 'c', 'i', 'J', 'p', 'S', 'r', 't', 'v'])
s4 = set('Node.js')
print s2 | s3 | s4  # set(['a', 'c', 'j', 'e', 'd', 'i', 'J', 's', 'o', '.', 'p', 'S', 'r', 't', 'v', 'N'])

# 4.补集
print s - set('py')  # set(['h', 't', 'o', 'n'])

# 5.异或
s5 = set('tool')
s6 = set('tools')
print s5 ^ s6  # set(['s'])
