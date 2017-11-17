#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/14 下午4:25
# @Author  : Aries
# @Site    : 
# @File    : py029_list_cmp.py
# @Software: PyCharm
'''
list 内建函数 cmp 和 len

'''

# cmp
arr1 = [1, 2]
arr2 = [3, 4]
print cmp(arr1, arr2)  # -1
print cmp(arr2, arr1)  # 1
# cmp原理,姑且是参数1是否大于参数2,若是怎返回1,否则返回2

# 判断两者若是相等
arr3 = [1, 2]
print cmp(arr1, arr3)  # 相等则返回0

# 若是两种不同类型的元素的列表相比较呢?
arr4 = ['1', '2']
print cmp(arr4, arr1)  # 1
print cmp(arr1, arr4)  # -1

arr5 = ['3', '4']
print cmp(arr5, arr1)  # 1
print cmp(arr4, arr5)  # -1
print cmp(arr5, ['3', '4']) # 0

# 数组长度 len
print len(arr1) # 2

