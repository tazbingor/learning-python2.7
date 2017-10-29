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
自然数n，符合（2的n次方－1）是质数，那么(2^p-1）X2^（p-1)是完全数
也就是说,这个数必须是偶数,且必须是6,或8结尾的数
'''

l = []
for n in range(1, 10000):
    for a in range(1, n):
        if n % a == 0:
            l.append(a)
    if sum(l) == n:
        print (n)
    l = []