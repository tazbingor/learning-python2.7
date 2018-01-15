#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午6:36
# @Author  : Aries
# @Site    : 
# @File    : py156_match_complex.py
# @Software: PyCharm
'''
15-10 匹配全体Python复数的字符串表示形式的集合
'''
import re


def match_complex(string=''):
    try:
        regex = r'^((\+|-)?(\d+\.?\d*|\d*\.?\d+)((e|E)(\+|-)?\d+)?){1,2}(j|J)$'
        return re.match(regex, string).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    print match_complex('123-12j')  # 123-12j
