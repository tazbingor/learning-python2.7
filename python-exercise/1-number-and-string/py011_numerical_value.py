#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/3 下午3:37
# @Author  : Aries
# @Site    : 
# @File    : py011_numerical_value.py
# @Software: PyCharm
# 数值形式回答下列问题

# 为什么17+32等于49,而017+32等于47,017+032等于41?
print 17 + 32
print 017 + 32  # 47
print 017 + 032  # 41
# 因为0开头的数,在Python中默认为八进制,所以后两个运算皆为八进制的运算
print int('017', 8) + 32  # 47
print int('017', 8)  # 15

# 为什么561+781的结果是134L而不是1342?
print 561 + 781  # 1342
print 56L + 78L
