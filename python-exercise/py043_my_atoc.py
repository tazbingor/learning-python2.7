#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/17 下午5:56
# @Author  : Aries
# @Site    : 
# @File    : py043_my_atoc.py
# @Software: PyCharm
'''
字符串.string模块包含三个函数，atoi()，atol()和atof()，他们分别负责把字符串转换成整型、长整型和浮点型数字。
从Python 1.5起，Python的内建函数int()、long()、float()也可以做同样的事了，本文来，complex()函数可以把字符串转换成复数
（然而1.5之前，这些转换函数只能工作于数字之上）

string模块中并没有实现一个atoc()函数，那么你来实现一个atoc()，接受单个字符串做参数输入，一个表示复数的字符串，
例如'-1.23e+4-5.67j'，返回相应的复数对象。
你不能用eval()函数，但可以使用complex()函数，而且你只能在如下的限制之下使用：complex():complex(real, imag)的real和imag都必须是浮点值。

'''
# atoc 接受单个字符参数输入,一个复数字符串,返回一个复数对象

def myAtoc(complexStr):
    pass
