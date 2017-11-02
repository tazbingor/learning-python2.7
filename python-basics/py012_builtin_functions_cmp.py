#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/2 上午10:58
# @Author  : Aries
# @Site    : 
# @File    : py012_builtin_functions_cmp.py
# @Software: PyCharm

'''
python 内建对象 cmp() 比较函数
比较两个对象(x,y)的大小,
若前者大于后者则返回1,或者一个正整数
若后者大于前者则返回-1,或者一个负整数
相等则为0

'''

a, b = 1, 2
print cmp(a, b)  # -1
print cmp(b, a)  # 1

print cmp(1, 1)  # 0

str1 = 'Python'
str2 = 'PHP'
print cmp(str1, str2)  # 1
print cmp(str2, str1)  # -1s

arr = [3, 7, 5, 9, 0]
arr.sort(cmp)
print arr  # [0, 3, 5, 7, 9]
