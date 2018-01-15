#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/12 下午5:47
# @Author  : Aries
# @Site    : 
# @File    : py151_match_address.py
# @Software: PyCharm
'''
15-5 匹配住址.
    1180 Bordeaux Drive
    3120 De la Cruz Boulevard
'''
from re import match


def match_address(address=''):
    try:
        return match(r'^[\u4E00-\u9FA5A-Za-z0-9_ ]+$', address).group()
    except AttributeError:
        return None


def match_chinese_address(address=''):
    try:
        return match(ur'^[\u4E00-\u9FA5A-Za-z0-9_ ]+$', address).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    print match_address('1180 Bordeaux Drive')  # 3120
    print match_address('3120 De la Cruz Boulevard')  # 3120 De la Cruz Boulevard
    for i in match_chinese_address(u'新街口南大街 百花深处胡同'):
        print i,
