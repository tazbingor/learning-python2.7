#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/7 下午4:44
# @Author  : Aries
# @Site    : 
# @File    : py023_number_triangle_02.py
# @Software: PyCharm
'''
数字三角形
样式2

'''
col = 0
while col < 6:  # 小于六行
    col += 1
    item = 1
    while item <= 6 - col:  # 每一行减少一个元素
        print item,
        item += 1
    print

print
