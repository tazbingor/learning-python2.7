#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午6:47
# @Author  : Aries
# @Site    : 
# @File    : py157_match_email.py
# @Software: PyCharm
'''
15-11.匹配所有的合法电子邮件地址
'''
import re


def match_email(string=''):
    try:
        regex = r'^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
        return re.match(regex, string).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    print match_email('python@qq.com')  # python@qq.com
