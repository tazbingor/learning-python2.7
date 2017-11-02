#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/2 上午10:58
# @Author  : Aries
# @Site    : 
# @File    : py012_builtin_functions_cmp.py
# @Software: PyCharm

'''
python 内建对象 str(), repr() 以及 ``
均将对象转换为字符串

'''

a = 88
result_a = str(a)
print result_a
print type(result_a)  # <type 'str'>

repr_a = repr(a)
print type(repr_a)  # <type 'str'>
print type(eval(repr_a))  # <type 'int'>

# ` 反单引号 也叫重音符
str1 = `a`
print type(str1)  # <type 'str'>
print type(`[1, 2, 3, 4, 5]`)  # <type 'str'>
print type(`type(1)`)  # <type 'str'>
