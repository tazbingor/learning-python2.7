#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午8:22
# @Author  : Aries
# @Site    : 
# @File    : py169_group_time.py
# @Software: PyCharm
'''
15-23.只提取时间戳中的时间。
'''
import re


def group_time(file_obj):
    for line in file_obj:
        m = re.match('.+(\d\d:\d\d:\d\d)', line)
        if m is not None:
            return m.group(1)


def get_time(path):
    with open(path) as f:
        return group_time(f)


if __name__ == '__main__':
    print get_time('redata.txt')  # 19:25:30
