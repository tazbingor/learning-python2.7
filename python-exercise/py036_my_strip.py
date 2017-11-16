#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/16 下午6:31
# @Author  : Aries
# @Site    : 
# @File    : py036_my_strip.py
# @Software: PyCharm
'''
自定义一个strip()方法,实现string strip的功能

1.去掉字符串前后的空格
2.保留字符串中间个空格

创建一个lstrip 和 rstrip方法

'''

str = '  A B C  '

# 去除左边空格
def leftStrip(arr):
    temp = list(arr)
    str_list = []
    isChart = True  # 遇见非空格字符标识
    for i in temp:
        if isChart:
            if i != ' ':
                isChart = False
                str_list.append(i)
        else:
            str_list.append(i)

    return str_list


# 去除右边空格
def rightStrip(arr):
    temp = list(arr)
    str_list = []
    isChart = True  # 遇见非空格字符标识
    for i in reversed(temp):
        if isChart:
            if i != ' ':  # 遇到第一个非空格字符时
                isChart = False
                str_list.append(i)
        else:
            str_list.append(i)

    str_list.reverse()
    return str_list


def myStrip(arr):
    return rightStrip(leftStrip(arr))


# Test
print ''.join(myStrip(str))
print ''.join(myStrip('  python Django  '))
# print ''.join(str)