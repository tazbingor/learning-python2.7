#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午6:16
# @Author  : Aries
# @Site    : 
# @File    : py155_match_float.py
# @Software: PyCharm
'''
15-9.匹配全体Python浮点型的字符串表示的集合。
'''
import re


def match_long(string=''):
    try:
        return re.match(r'^(\+|-)?(\d+\.\d*|\d*\.\d+ )((e|E)(\+|-)?\d+)?$', string).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    print match_long('998.99')  # 998.99
