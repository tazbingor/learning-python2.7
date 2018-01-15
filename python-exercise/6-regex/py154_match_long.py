#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午6:10
# @Author  : Aries
# @Site    : 
# @File    : py154_match_long.py
# @Software: PyCharm
'''
15-8 匹配长整形
'''
import re


def match_long(string=''):
    try:
        return re.match(r'^(\+|-)?((0|[1-9]\d*)|(0[xX][0-9a-fA-F]+))$', string).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    print match_long('384')  # 384
