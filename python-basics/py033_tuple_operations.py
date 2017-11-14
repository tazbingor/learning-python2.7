#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/14 下午7:40
# @Author  : Aries
# @Site    : 
# @File    : py033_tuple_operations.py
# @Software: PyCharm
'''
元组操作与内建函数

因为元组不可变,所以增删改等诸多liet通用的内建函数在元组上显得毫无意义
所以只能用原始的方式进行修改
'''

num_tuple = (2, 4)
print num_tuple * 2  # (2, 4, 2, 4)
print num_tuple * 3  # (2, 4, 2, 4)
# num_tuple += (1, 3)
# print num_tuple # (2, 4, 1, 3)

# num_tuple *= num_tuple # 元组间不能相乘除
# print num_tuple

# in
print 1 in num_tuple  # False
print 2 in num_tuple  # True

num_tuple = (2, 4, 6, 8)

# min() and max()
print min(num_tuple)  # 2
print max(num_tuple)  # 8

# len
print len(num_tuple)  # 4

print "-" * 50
# 默认集合类型
print 1, 4, 'w', 9.0
x, y, z = 1, 2, 3
print x, y, z

# 单元素元组
str_tuple = ('A')
print type(str_tuple)  # <type 'str'>
num_tuple = (99)
print type(num_tuple)  # <type 'int'>
