#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/19 下午5:40
# @Author  : Aries
# @Site    : 
# @File    : py044_set_operator.py
# @Software: PyCharm
'''
可变集合操作符
'''
# update 更新
s = set('python')
s |= set('A')
print s  # set(['A', 'h', 'o', 'n', 'p', 't', 'y'])

# 保留,交集更新 保留两集合的相同元素
s2 = set('jpython')
s2 &= s
print  s2  # set(['h', 'o', 'n', 'p', 't', 'y'])

# 差更新
s3 = set('python')
s3 -= set('p')
print s3  # set(['h', 'o', 'n', 't', 'y'])

# 差分跟新
s4 = set('Java')
s5 = set('JavaScript')
s5 ^= s4
print s5  # set(['c', 'i', 'p', 'S', 'r', 't'])
