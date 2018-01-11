#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/11 下午9:12
# @Author  : Aries
# @Site    : 
# @File    : py011_regex_example_02.py
# @Software: PyCharm
'''
例题2: split 根据匹配进行切割字符串，并返回一个列表

'''
import re


def str_split(string=''):
    return re.split(r':| ', string)


if __name__ == '__main__':
    string = 'python:2.7 python 3.6'
    print str_split(string)  # ['python', '2.7', 'python', '3.6']
