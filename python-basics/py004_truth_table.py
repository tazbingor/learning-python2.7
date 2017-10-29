#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/29 上午10:53
# @Author  : Aries
# @Site    : 
# @File    : py004_truth_table.py
# @Software: PyCharm
# 真值表

str_truth = "x  y  x and y  x or y"
length = len(str_truth)

print str_truth
print  length * '-'

for x in [True, False]:
    for y in [True, False]:
        print "%-9s %-9s %-9s %-9s" % (x, y, (x and y), (x or y))
