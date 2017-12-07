#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/7 下午5:11
# @Author  : Aries
# @Site    : 
# @File    : py069_filter.py
# @Software: PyCharm
'''
filter()
调用一个布尔函数func来迭代遍历每个seq中的元素;返回一个使func返回值为true的元素序列
相当于一个筛子用来过滤一个函数
'''


# 实现filter
def myFilter(bool_func, seq):
    result_seq = []
    for eachItem in seq:
        if bool_func(eachItem):
            result_seq.append(eachItem)
    return result_seq
