#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/3 下午6:46
# @Author  : Aries
# @Site    : 
# @File    : py139_raw_input_evo.py
# @Software: PyCharm
'''
10-8.改进raw_input
'''


def safe_input(example):
    stamp = None
    try:
        stamp = raw_input(example)
    except KeyboardInterrupt:
        pass
    return stamp


if __name__ == '__main__':
    print safe_input('please input: ')
