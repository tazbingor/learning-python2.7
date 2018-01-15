#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午5:50
# @Author  : Aries
# @Site    : 
# @File    : py153_match_int.py
# @Software: PyCharm
'''
15-7.匹配全体Python整型的字符串表示形式的集合。
'''
import re


def match_int(string=''):
    try:
        return re.match(r'-?\d+', string).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    print match_int('12')
