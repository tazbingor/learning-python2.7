#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午3:43
# @Author  : Aries
# @Site    : 
# @File    : py098_function_01.py
# @Software: PyCharm
'''
11-2 函数。结合你对练习5-2的解，以便你创建一个带一对相同数字并同时返回它们之和以及产物的结合函数。

'''


# 普通
def numAdd(a, b):
    return a + b


# 函数式
num_add = lambda x, y: x + y

if __name__ == '__main__':
    print '一般函数,', numAdd(1, 2)  # 3
    print '函数式,', num_add(1, 2)  # 3
