#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/13 下午 09:59
# @Author  : Aries
# @Site    : 
# @File    : py091_class_attribute.py.py
# @Software: PyCharm

'''
类属性
'''


class C(object):
    foo = 100

if __name__ == '__main__':
    # 简单引用类属性
    print C.foo  # 100

    C.foo += 1
    print C.foo  # 101
