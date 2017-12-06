#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午8:31
# @Author  : Aries
# @Site    : 
# @File    : py061_built-in_function.py
# @Software: PyCharm
'''
内部函数
'''


# 创建内部函数
def out_func():
    def in_func(a, b):
        return a * b

    return in_func(2, 2)


# 闭包了
# print in_func(1, 2) # NameError: name 'in_func' is not defined
print out_func()  # 4


