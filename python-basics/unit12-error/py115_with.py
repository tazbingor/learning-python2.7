#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/2 下午7:56
# @Author  : Aries
# @Site    : 
# @File    : py115_with.py
# @Software: PyCharm
'''
with 语句
'''


def my_open(path, opt='r'):
    with open(path, opt) as f:
        for eachLine in f:
            print eachLine


if __name__ == '__main__':
    my_open('py112_try_except.py')
