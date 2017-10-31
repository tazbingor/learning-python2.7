#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/31 上午11:52
# @Author  : Aries
# @Site    : 
# @File    : py005_number_triangle.py
# @Software:
# 实现数字指直角三角形

'''
1
12
123
1234
12345
123456
.......
输如你想得到的行数
'''

num = raw_input("请输入你想要的行数\n")
item = 1
while item < int(num):
    item += 1
    col = 1
    while col < item:
        print col,
        col += 1
    print
