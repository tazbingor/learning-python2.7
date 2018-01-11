#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/11 下午7:53
# @Author  : Aries
# @Site    : 
# @File    : py007_search.py
# @Software: PyCharm
'''
re高级模块

search 函数将对整个字符串进行搜索，并返回第一个匹配的字符串的match对象。
'''

import re


def str_count(string):
    return re.search('\\d*[.]\\d*', string).group()


if __name__ == '__main__':
    # 查找字符串中的数字
    print str_count('当前使用的python版本为3.5')  # 3.5
