#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/29 上午11:40
# @Author  : Aries
# @Site    : 
# @File    : py002_perfect_number.py
# @Software: PyCharm

'''
找出10000以内的完全数

6 = 1 + 2 + 3
28 = 1 + 2 + 3 + 7 + 14
自然数n，符合（2的n次方－1）是质数，那么（2的n次方－1）*（2的n-次方）是完全数
'''

n = 1
while n < 10000:
    if n / n == 1 and n / 1 == n \
            and n == (2 ** (n - 1)) * (2 ** n):
        print str(n) + "是完全数"
    n += 1
    # print n
