#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/30 下午10:53
# @Author  : Aries
# @Site    : 
# @File    : py114_multiple_except.py
# @Software: PyCharm
'''
带有许多except 的try语句
'''


def safe_float(obj):
    try:
        retval = float(obj)
    except ValueError:
        retval = 'could not convert non-number to float'
    except TypeError:
        retval = 'object type connot be converted to float'
    return retval


if __name__ == '__main__':
    print safe_float('xyz')  # could not convert non-number to float

    print safe_float([])  # object type connot be converted to float

    print safe_float(())  # object type connot be converted to float

    print safe_float(200)  # 200.0

    print safe_float(89.69)  # 89.69
