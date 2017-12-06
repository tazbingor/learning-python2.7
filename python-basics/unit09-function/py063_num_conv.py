#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午9:38
# @Author  : Aries
# @Site    : 
# @File    : py063_num_conv.py
# @Software: PyCharm
'''
传递和调动(内建函数)
'''


def convert(func, seq):
    return [func(eachNum) for eachNum in seq]


myseq = (123, 45.67, -6.2e8, 99999999L)
print convert(int, myseq)  # [123, 45, -620000000, 99999999]
print convert(long, myseq)  # [123L, 45L, -620000000L, 99999999L]
print convert(float, myseq)  # [123.0, 45.67, -620000000.0, 99999999.0]
