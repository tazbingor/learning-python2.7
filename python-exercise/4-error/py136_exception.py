#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/3 下午6:18
# @Author  : Aries
# @Site    : 
# @File    : py136_exception.py
# @Software: PyCharm
'''
10-5 异常
    下面这些交互解释器下的Python代码段分别会引发什么异常
'''
# if 3 < 4 then:print '3 is less than 4!' # SyntaxError: invalid syntax
aList = ['Hello', 'World', 'Anyone', 'Home?']
# print 'the last string in aList is: ', aList[len(aList)]  # IndexError: list index out of range
# x # NameError: name 'x' is not defined

# x = 4 % 0 # ZeroDivisionError: integer division or modulo by zero

import math

# i = math.sqrt(-1) # ValueError: math domain error
