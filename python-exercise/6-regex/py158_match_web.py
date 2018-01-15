#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午6:54
# @Author  : Aries
# @Site    : 
# @File    : py158_match_web.py
# @Software: PyCharm
'''
15-12.匹配所有合法的Web网站地址。
'''
import re


def match_web(string=''):
    try:
        regex = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'
        return re.match(regex, string).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    print match_web('www.python.com')  # www.python.com
