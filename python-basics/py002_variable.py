#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/28 下午12:18
# @Author  : Aries
# @Site    : 
# @File    : py002_variable.py
# @Software: PyCharm
# 变量

a = 'hello'
b = a
a = 100;
# id() 返回当前对象的唯一ID, 在Cpython解释器中描述为内存地址
print id(a)
print id(b)
print a, '\t', b, '\n'

print type(a), type(b)

