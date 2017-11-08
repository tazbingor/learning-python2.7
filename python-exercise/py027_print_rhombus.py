#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/8 下午2:50
# @Author  : Aries
# @Site    : 
# @File    : py027_print_rhombus.py
# @Software: PyCharm
'''
输出菱形


'''

star = 1
num = int(raw_input("请输入15以内的数\n"))
col = num
i = 0
while i < num:  # 上金字塔
    print ' ' * col, '*' * star
    col -= 1
    star += 2
    i += 1

col = 0
j = 0
while j < num + 1:  # 逆金字塔
    print ' ' * col, '*' * star
    col += 1
    star -= 2
    j += 1
