#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午8:18
# @Author  : Aries
# @Site    : 
# @File    : py167_group_month.py
# @Software: PyCharm
'''
15-21.只提取时戳中的月份。
'''
import re


def group_month(file_obj):
    for line in file_obj:
        m = re.match('.+? (.+?) .+', line)
        if m is not None:
            return m.group(1)


def get_month(path):
    with open(path) as f:
        return group_month(f)


if __name__ == '__main__':
    print get_month('redata.txt')  # Aug
