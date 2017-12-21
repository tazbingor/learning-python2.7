#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/7 下午5:15
# @Author  : Aries
# @Site    :
# @File    : py024_number_triangle_03.py
# @Software: PyCharm
'''
样式三

'''

i = 0
j = 0
num = 6
while i < num:
    i += 1
    j = i
    arr = []
    count = 0

    # 插入空格符
    while count < num - j:
        arr.append(" ")
        count += 1

    while j >= 1:
        # print str(j),
        arr.append(str(j))  # 尾部插入數值
        j -= 1
    result = "".join(arr)  # 數組轉字符串
    print result
