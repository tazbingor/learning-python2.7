#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/2 下午5:53
# @Author  : Aries
# @Site    : 
# @File    : py019_number_functions_difference.py
# @Software: PyCharm

'''
数字内建函数之间的差异

int(),round(),math.foolr()之间的差异
差异
int()直接截去小数部分
round()得到接近原型的浮点型
math.floor()得到接近原数但小于原数的整型
'''

import math

arr = [0.2, 0.7, 1.2, 1.7, -0.2, -0.7, -1.2, -1.7]
for eachNumber in arr:
    print "int(%.1f)\t\t%+.1f" % (eachNumber, float(int(eachNumber)))
    print "floor(%.1f)\t\t%+.1f" % (eachNumber, math.floor(eachNumber))
    print "round(%.1f)\t\t%+.1f" % (eachNumber, round(eachNumber))
    print '-' * 30
