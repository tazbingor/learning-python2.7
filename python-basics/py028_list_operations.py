#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/13 下午5:06
# @Author  : Aries
# @Site    : 
# @File    : py028_list_operations.py
# @Software: PyCharm
'''
list 操作符
'''

# 标准类型操作符
arr1 = ['abc', 123]
arr2 = ['xyz', 789]
arr3 = ['abc', 123]

print arr1 == arr3  # True
print arr1 == arr2  # False
print arr1 > arr2  # False
print arr1 < arr2  # True
print arr1 < arr2 and arr1 == arr3  # True
print

# # test 列表相乘
# numList1 = [2, 4, 6]
# numList2 = [3, 5, 7]
# result = numList1 * numList2
# print result


# 成员关系操作 in,not in
mixup_list = [4.0, [1, 'x'], 'beef', (-1.9 + 6j)]
print 'beef' in mixup_list  # True
print 'x' in mixup_list  # False
print 'x' in mixup_list[1]  # True
print
num_list = [[65535L, 2e+030, (76.45 - 1.)], -1.23, 16.0, -49]
print -49 in num_list  # True
print 34 in num_list  # False
print 65535L in num_list[0]  # True
print
num_tuple = (1, 2, 3, 4, (1, 2, 3))
print 1 in num_tuple  # True
print 1 in num_tuple[4]  # True
print

# 连接操作符(+)
print mixup_list + num_list
# print num_list + num_tuple # 元组与列表不能连接
print

# 列表切片
str_list = ['A', 'B', 'C', 'D', 'E']
print str_list[:1]  # ['A']
print str_list[0:3]  # ['A', 'B', 'C']
print str_list[:4]  # ['A', 'B', 'C', 'D']
print


