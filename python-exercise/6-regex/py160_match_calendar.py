#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午7:06
# @Author  : Aries
# @Site    : 
# @File    : py160_match_calendar.py
# @Software: PyCharm
'''
15-14 请写出一个正则表达式表示标准日历上的月份。
'''
import re


def match_calendar(string=''):
    try:
        regex = r'^(0?[1-9])$|^(10|11|12)$'
        return re.match(regex, string).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    print match_calendar('10')  # 10
