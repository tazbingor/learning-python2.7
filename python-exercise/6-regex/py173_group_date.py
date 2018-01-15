#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午8:49
# @Author  : Aries
# @Site    : 
# @File    : py173_group_date.py
# @Software: PyCharm
'''
15-27.提取出时间戳中的月、日、年，并按照格式“月 日，年”输出，且每行仅遍历一次。
'''
import re


def get_data(path):
    with open(path) as f:
        for line in f:
            m = re.match('\w+ (\w+ \w+) .+ (\d+)', line)
            if m is not None:
                return '%s, %s' % (m.group(1), m.group(2))


if __name__ == '__main__':
    print get_data('redata.txt')  # Aug 28, 2047
