#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/11 下午7:58
# @Author  : Aries
# @Site    : 
# @File    : py008_findall.py
# @Software: PyCharm
'''
re 高级用法

findall 函数将返回一个所有匹配的字符串的字符串列表。
'''
import re


def str_list(string):
    return re.findall('\\d*[.]\\d*', string)


if __name__ == '__main__':
    # 查找字符串中的数字
    print str_list('当前使用的python版本为2.7,推荐使用python3.5或者3.6版本')  # ['2.7', '3.5', '3.6']

