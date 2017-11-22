#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 下午2:26
# @Author  : Aries
# @Site    : 
# @File    : py063_range.py
# @Software: PyCharm
'''
8.3 range(). 如果我们需要生成下面的这些列表,分别需要在range()内建函数中提供哪些
   参数?
   a) [0,1,2,3,4,5,6,7,8,9]
   b) [3,6,9,12,15,18]
   c) [-20,200,420,640,860]

'''

# a) [0,1,2,3,4,5,6,7,8,9]
print [i for i in range(10)]

# b) [3, 6, 9, 12, 15, 18]
print [i for i in range(3, 21, 3)]

# c) [-20,200,420,640,860]
print [i for i in range(-240, 1000, 220)]
