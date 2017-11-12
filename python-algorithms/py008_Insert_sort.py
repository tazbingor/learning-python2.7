#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/12 下午7:06
# @Author  : Aries
# @Site    : 
# @File    : py008_Insert_sort.py
# @Software: PyCharm
'''
插入排序
'''

arr = [3, 49, 100, 66, 24, 99, 76, 0, 88, 56]

for i in range(1, len(arr)):
    if arr[i - 1] > arr[i]:
        temp = arr[i]  # 当前需要排序的元素
        index = i  # 用来记录排序元素需要插入的位置
        while index > 0 and arr[index - 1] > temp:
            arr[index] = arr[index - 1]  # 把已经排序好的元素后移一位，留下需要插入的位置
            index -= 1
        arr[index] = temp  # 把需要排序的元素，插入到指定位置

print arr
