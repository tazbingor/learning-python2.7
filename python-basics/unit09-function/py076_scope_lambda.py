#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 上午10:17
# @Author  : Aries
# @Site    : 
# @File    : py076_scope_lambda.py
# @Software: PyCharm
'''
作用域与lambda
'''
x = 10


def foo():
    y = 5
    # bar = lambda: x + y

    bar = lambda y=y: x + y
    print bar(y)
    y = 8
    print bar(y)


foo()
