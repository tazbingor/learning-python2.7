#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/28 下午11:26
# @Author  : Aries
# @Site    : 
# @File    : py113_encapsulate_built_in_functions.py
# @Software: PyCharm
'''
封装內建函数

'''


def safe_float(obj):
    try:
        retval = float(obj)
    except ValueError:
        retval = 'could not convert non-number to float'
    return retval

if __name__ == '__main__':
    print safe_float('12.34')  # 12.34
    print safe_float('bad input') # could not convert non-number to float

