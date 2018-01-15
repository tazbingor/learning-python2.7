#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午8:08
# @Author  : Aries
# @Site    : 
# @File    : py165_group_timestamp.py
# @Software: PyCharm
'''
15-19 提取每行中完整的时间戳字段
'''
import re


def group_timestamp(file_obj):
    re_timestamp = re.compile(r'\w{3} \w{3} \d\d \d\d:\d\d:\d\d \d{4}')

    while True:
        line = file_obj.readline()
        if line:
            match = re_timestamp.match(line)
            return match.group()
        else:
            break


def timestamp(path):
    with open(path) as f:
        return group_timestamp(f)


if __name__ == '__main__':
    print timestamp('redata.txt')  # Wed Aug 28 19:25:30 2047
