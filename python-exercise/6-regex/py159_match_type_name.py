#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午6:58
# @Author  : Aries
# @Site    : 
# @File    : py159_match_type_name.py
# @Software: PyCharm
'''
15-13.写一个正则表达式，能从type()返回的字符串中提取类型的名字。

'''
import re


def match_type(resource):
    string = str(type(resource))
    try:
        regex = r'<type \'(\w+)\'>'
        return re.match(regex, string).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    print match_type(3.14)  # <type 'float'>
    print match_type(dir)  # <type 'builtin_function_or_method'>
