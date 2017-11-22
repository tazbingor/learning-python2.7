#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 下午1:42
# @Author  : Aries
# @Site    : 
# @File    : py050_generator_example.py
# @Software: PyCharm
'''
生成器举例
'''

# 交叉配对
rows = [1, 2, 3, 17]


def cols():
    yield 56
    yield 2
    yield 1


x_product_pairs = ((i, j) for i in rows for j in cols())
for pair in x_product_pairs:
    print  pair
