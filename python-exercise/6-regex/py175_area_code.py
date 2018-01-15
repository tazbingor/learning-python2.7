#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午8:59
# @Author  : Aries
# @Site    : 
# @File    : py175_area_code.py
# @Software: PyCharm
'''
15-29.区号中可以包含圆括号或连字符，而且它们是可选的，
就是说你写的正则表达式可以匹配800-555-1212、555-1212或(800)555-1212。
'''
import re


def area_code(tel=''):
    m = re.match(r'^(\d{3}-|\(\d{3}\))?\d{3}-\d{4}$', tel)
    if m is not None:
        return m.group()
    else:
        return 'Not match'


if __name__ == '__main__':
    print area_code('800-555-1212')  # 800-555-1212
    print area_code('555-1212')  # 555-1212
    print area_code('(800)555-1212')  # (800)555-1212
