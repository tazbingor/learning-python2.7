#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/10 下午4:36
# @Author  : Aries
# @Site    : 
# @File    : py007_bubble_sort_logogram.py
# @Software: PyCharm
'''
冒泡排序简写

'''
arr = [65, 29, 6, 54, 62, 88, 66, 108]
count = len(arr)
i = 0

while i < count - 1:
    j = 0

    while arr[j] > arr[j + 1]:  # 数组中,前一位大于后一位,则进行交换
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        j += 1
    i += 1
print arr
