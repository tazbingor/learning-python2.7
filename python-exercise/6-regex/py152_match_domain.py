#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/13 下午11:41
# @Author  : Aries
# @Site    : 
# @File    : py152_match_domain.py
# @Software: PyCharm
'''
15-6 匹配简单的url 以www. 开头,以.com结尾

'''
from re import match


def match_domain(str_url=''):
    try:
        return match(r'\bwww\..*\.(com|net|edu)', str_url).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    print match_domain('www.python.com')  # www.python.com
