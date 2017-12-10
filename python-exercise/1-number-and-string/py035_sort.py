#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/16 下午5:43
# @Author  : Aries
# @Site    : 
# @File    : py035_sort.py
# @Software: PyCharm
'''
排序
'''

# 1. 数字排序 ,从大到小排列
num_list = [23, 56, 32, 10, 88, 66]
length = len(num_list)
for i in range(length - 1):
    for j in range(length - 1 - i):
        if num_list[j] < num_list[j + 1]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

print num_list


# 2. 字符串以字典序排序
str_list = raw_input('请输入排序的字符串:\n')
# print type(str_list)
arr = list(str_list)
arr.sort()
str_list = ''.join(arr)
print str_list

