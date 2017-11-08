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
user_number = int(raw_input("请输入15以内的数字:\n"))
item = 1
while item <= user_number:
    num = user_number
    while num > item:  # 计算两边空格符的数量
        print ' ',
        num -= 1
    num = item
    while num >= 1:  # 计算金字塔左半边的数字
        print "*",
        num -= 1

    num = 2
    while num <= item:  # 计算金字塔又半边的数字
        print "*",
        num += 1

    item += 1
    print