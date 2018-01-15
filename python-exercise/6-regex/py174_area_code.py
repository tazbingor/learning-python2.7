#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午8:56
# @Author  : Aries
# @Site    : 
# @File    : py174_area_code.py
# @Software: PyCharm
'''
15-28.区号（第一组的三个数字和它后面的连字符）是可选的，
即你写的正则表达式对800-555-1212和555-1212都可匹配。
'''
import re


def area_code(tel=''):
    m = re.match('(\d{3}-)*\d{3}-\d{4}', tel)
    if m is not None:
        return m.group()
    else:
        return 'Not match'


if __name__ == '__main__':
    print area_code('800-555-1212')  # 800-555-1212
    print area_code('555-1212')  # 555-1212
