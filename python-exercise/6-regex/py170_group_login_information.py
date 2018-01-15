#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午8:25
# @Author  : Aries
# @Site    : 
# @File    : py170_group_login_information.py
# @Software: PyCharm
'''
15-24.只从电子邮件地址中提取出登录名和域名。
'''
import re


def group_information(file_obj):
    for line in file_obj:
        m = re.search(r'::([a-z]+)@([a-z]+\.[a-z]+)::', line)
        if m is not None:
            return ''.join([m.group(1), m.group(2)])


def get_information(path):
    with open(path) as f:
        return group_information(f)


if __name__ == '__main__':
    print get_information('redata.txt')  # zlzdpqmybv.org
