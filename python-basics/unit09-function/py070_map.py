#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/7 下午5:22
# @Author  : Aries
# @Site    : 
# @File    : py070_map.py
# @Software: PyCharm
'''
map()
map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。


'''


# 实现map

def myMap(func, seq):
    result_seq = []
    for eachItem in seq:
        result_seq.append(func(eachItem))
    return result_seq


print myMap((lambda x: x ** 2), [1, 2, 3, 4, 5, 6, 7, 8, 9])
