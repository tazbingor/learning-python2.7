#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/18 下午11:16
# @Author  : Aries
# @Site    : 
# @File    : py042_aggregate.py
# @Software: PyCharm
'''
python 集合

集合 aggregate 数学上为set ,集合元素为set elements
'''

# 创建集合 set()
s = set('python')
print s  # set(['h', 'o', 'n', 'p', 't', 'y'])
print type(s)  # <type 'set'>

# 创建集合 frozenset()
t = frozenset('python')
print t  # frozenset(['h', 'o', 'n', 'p', 't', 'y'])
print type(t)  # <type 'frozenset'>l

# 访问集合中的值
print 'p' in s  # True
print 'y' not in s  # False
print '-' * 50

# 跟新集合
# 添加
s.add('j')
print s  # set(['h', 'j', 'o', 'n', 'p', 't', 'y'])
s.update('b')
print s  # set(['b', 'h', 'j', 'o', 'n', 'p', 't', 'y'])
s.add('a')
print s  # set(['a', 'b', 'h', 'j', 'o', 'n', 'p', 't', 'y'])
# 删除元素
s.remove('b')
print s  # set(['a', 'h', 'j', 'o', 'n', 'p', 't', 'y'])
# 再次添加元素
s.add('b')
print s  # set(['a', 'b', 'h', 'j', 'o', 'n', 'p', 't', 'y'])
# 对字符串元素而言,集合储存字符串元素会以字典序重新排列集合成员
s.add('rich')
print s  # set(['a', 'b', 'h', 'j', 'o', 'n', 'p', 't', 'rich', 'y'])
print '-' * 50

# frozenset()集合不能被修改
# print t
# t.add('a')
# print t
