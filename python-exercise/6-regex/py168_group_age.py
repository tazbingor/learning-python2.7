#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午8:20
# @Author  : Aries
# @Site    : 
# @File    : py168_group_age.py
# @Software: PyCharm
'''
15-22.只提取时间戳中的年份。
'''
import re


def group_age(file_obj):
    for line in file_obj:
        m = re.match('.+ (.+?)::', line)
        if m is not None:
            return m.group(1)


def get_age(path):
    with open(path) as f:
        return group_age(f)


if __name__ == '__main__':
    print get_age('redata.txt')  # 2047
