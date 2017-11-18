#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/18 下午5:20
# @Author  : Aries
# @Site    : 
# @File    : py038_aggregate_functions.py
# @Software: PyCharm
'''
集合类型内建函数
'''

import copy

dict1 = {
    2: 'two',
    4: 'four',
    6: 'six',
    8: 'eight'
}

dict2 = {
    2: 'two',
    4: 'four',
    6: 'six'
}

# py2 cmp()
print cmp(dict1, dict2)  # 1
print cmp(dict2, dict1)  # -1
print cmp(dict1[2], dict2[2])  # 0

# 比较字符串长度
print len(dict1) > len(dict2)  # True
print len(dict2) > len(dict1)

# dict()
print dict(zip(('x', 'y', 'z'), ('1', '2', '3')))  # {'y': '2', 'x': '1', 'z': '3'}
print dict([['x', '1'], ['y', '2']])  # {'y': '2', 'x': '1'}
print dict([('xy'[i - 1], i) for i in range(1, 3)])  # {'y': 2, 'x': 1}
print  '-' * 50

# 修改字典
dict3 = {'x': 1, 'y': 2}
dict3 = dict(x=3, y=4)
print dict3  # {'y': 4, 'x': 3}
# 复制字典
dict4 = dict(**dict3)
print dict4  # {'y': 4, 'x': 3}
# 使用copy() 浅拷贝
dict5 = dict4.copy()
print dict5  # {'y': 4, 'x': 3}
# 深拷贝
dict6 = copy.deepcopy(dict5)
print dict6 # {'y': 4, 'x': 3}
