#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/12 下午5:39
# @Author  : Aries
# @Site    : 
# @File    : py150_match_identifier.py
# @Software: PyCharm
'''
15-4 匹配Python中所有合法的标识符
'''
from re import match


def match_identifier(string=''):
    try:
        return match(r'^[_A-za-z][_\w]*', string).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    # 测试
    print match_identifier('_age')  # _age
    print match_identifier('match_identifier')  # match_identifier
    print match_identifier('matchIdentifier')  # matchIdentifier
