#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/10 下午3:49
# @Author  : Aries
# @Site    : 
# @File    : py006_bubble_sort.py
# @Software: PyCharm

'''
冒泡排序
'''

arr = [65, 29, 6, 54, 62, 88, 66, 108]
count = len(arr)
i = 0
while i < count - 1:
    j = 0
    while j < count - 1 - i:
        temp = 0
        if arr[j] > arr[j + 1]:  # 数组中,前一位大于后一位,则进行交换
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
        j += 1
    i += 1


# 变量交换
def variateSwap(num1, num2):
    # temp = 0  # 临时交换变量
    temp = num1
    num1 = num2
    num2 = temp


print arr
