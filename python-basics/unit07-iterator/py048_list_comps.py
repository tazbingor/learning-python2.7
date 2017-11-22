#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 上午11:43
# @Author  : Aries
# @Site    : 
# @File    : py048_list_comps.py
# @Software: PyCharm
'''
列表解析
'''
import os

# lambda 计算成员平方
print [x ** 2 for x in range(6)]  # [0, 1, 4, 9, 16, 25]

print map(lambda x: x ** 2, range(6))  # [0, 1, 4, 9, 16, 25]

# lambda 挑选基数
seq = [i for i in range(100)]
print filter(lambda x: x % 2, seq)
print [x for x in seq if x % 2]

# 使用迭代器获得3X5的矩阵
print [(x + 1, y + 1) for x in range(3) for y in range(5)]

# 计算文件空白字符
file = open('py045_iterator.py', 'r')
print len([word for line in file for word in line.split()])  # 73
file.close()

# 快速计算文件大小
print os.stat('py045_iterator.py').st_size  # 489
