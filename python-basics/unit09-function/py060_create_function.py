#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午8:16
# @Author  : Aries
# @Site    : 
# @File    : py060_create_function.py
# @Software: PyCharm
'''
创建函数
    1.前向引用:py不允许在函数未声明钱,对其进行调用
    2.函数属性:倘若在模块A或模块B中有相同变量名c,导入后仍然可以使用其变量.

'''


def A():
    c = 1


def B():
    c = 2


# class A:
#     c = 'P'
#
#
# class B:
#     c = 'Y'


print A().c  # 1
print B().c  # 2

# print A.c  #
# print B.c  #
