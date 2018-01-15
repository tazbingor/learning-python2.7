#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午8:14
# @Author  : Aries
# @Site    : 
# @File    : py166_group_email.py
# @Software: PyCharm
'''
15-20 提取每行中完整的电子邮件地址
'''
import re


def group_email(file_obj):
    for line in file_obj:
        m = re.match('.+::(.+)::(\d+)', line)
        if m is not None:
            return m.group(1)


def get_email(path):
    with open(path) as f:
        return group_email(f)


if __name__ == '__main__':
    print get_email('redata.txt')  # zlzdp@qmybv.org
