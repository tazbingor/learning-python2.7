#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/12 下午5:25
# @Author  : Aries
# @Site    : 
# @File    : py148_match_name_01.py
# @Software: PyCharm
'''
15-2 匹配用空格分隔的任意一对单词,比如姓名
(返回一个list)
'''
import re


def match_name(string):
    try:
        return re.split(r' ', string)
    except AttributeError:
        return None


if __name__ == '__main__':
    # 测试
    print match_name('Bruce Wayne')  # ['Bruce', 'Wayne']
    print match_name('Barack Hussein Obama')  # ['Barack', 'Hussein', 'Obama']
