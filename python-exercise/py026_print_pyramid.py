#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/7 下午8:30
# @Author  : Aries
# @Site    : 
# @File    : py026_print_pyramid.py
# @Software: PyCharm

'''
输出金字塔
只能 while和print语句输出下 的图样
        *
       ***
      *****
     *******
    *********
'''

'''
方法一
'''
user_number = int(raw_input("方法二,请输入15以内的数字:\n"))
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

print "-" * 50

'''
方法二
'''
star = 1
num = int(raw_input("方法一,请输入15以内的数\n"))
col = num
i = 0
while i < num:  # 上金字塔
    print ' ' * col, '*' * star
    col -= 1
    star += 2
    i += 1
