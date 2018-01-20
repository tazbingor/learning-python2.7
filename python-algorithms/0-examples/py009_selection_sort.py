#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/12 下午7:29
# @Author  : Aries
# @Site    : 
# @File    : py009_selection_sort.py
# @Software: PyCharm
'''
选择排序
将每一个元素与剩下的元素进行比较,若小于,则交换
'''
arr = [3, 49, 100, 66, 24, 99, 76, 0, 88, 56]

num = len(arr)
print num

for i in range(num):
    small = i
    for j in range(i + 1, num):
        if arr[j] < arr[small]:  # 若轮到下一位元素的值小于最小的数,则代替它
            small = j
    if small != i:
        arr[i], arr[small] = arr[small], arr[i]
print arr
