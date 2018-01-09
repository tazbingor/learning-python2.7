#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/9 下午6:50
# @Author  : Aries
# @Site    : 
# @File    : py005_periphery.py
# @Software: PyCharm
'''
表示边界

    ^   匹配字符串开头
    $   匹配字符串结尾
    \b  匹配一个单词的边界
    \B  匹配一个非单词的边界
'''
import re


def re_email163(email):
    re_string = r'^[\w]{4,20}@163\.com$'

    try:
        result = re.match(re_string, email)
        return result.group()
    except AttributeError:
        return None


def re_periphery(string):
    re_string = r'.*thon\b'

    try:
        result = re.match(re_string, string)
        return result.group()
    except AttributeError:
        return None


def re_not_periphery(string):
    re_string = r'.*\Bthon\B'

    try:
        result = re.match(re_string, string)
        return result.group()
    except AttributeError:
        return None


if __name__ == '__main__':
    # 匹配163邮箱
    print re_email163('python@163.com')  # python@163.com

    #  \b  匹配一个单词的边界
    print re_periphery('Py thon')  # Py thon

    #  \B  匹配一个非单词的边界
    print re_not_periphery('pythonic') # python
