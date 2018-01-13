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
        return match(r'^', address).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    pass
