#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/12 下午5:30
# @Author  : Aries
# @Site    : 
# @File    : py149_match_name_02.py
# @Software: PyCharm
'''
15-3 匹配用一个逗号和一个空格分开的一个单词和一个字母.还是名字
(默认返回单词)
'''
import re


def match_name(name=''):
    try:
        return re.split(r' |,?', name)
    except AttributeError:
        return None


if __name__ == '__main__':
    # 测试
    print match_name('Martin Luther King')  # ['Martin', 'Luther', 'King']

    print match_name('This is our hope, and this is the faith that I go back to the South with.')
    # ['This', 'is', 'our', 'hope', '', 'and', 'this', 'is', 'the', 'faith', 'that', 'I', 'go', 'back', 'to', 'the', 'South', 'with.']
