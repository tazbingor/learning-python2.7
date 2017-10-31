#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/30 上午11:13
# @Author  : Aries
# @Site    : 
# @File    : py003_factorial.py
# @Software: PyCharm

# 求阶乘

input_number = int(input())
result = 1
for item in range(2, input_number + 1):
    result *= item
print result
