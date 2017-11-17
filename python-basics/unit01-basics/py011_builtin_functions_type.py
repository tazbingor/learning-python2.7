#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/2 上午10:41
# @Author  : Aries
# @Site    : 
# @File    : py011_builtin_functions_type.py
# @Software: PyCharm

'''
python 标准内建函数
'''

# type() 返回一个对象的类型
print type(0)  # <type 'int'>
print type(1)  # <type 'int'>
print type(1L)  # <type 'long'>

print type(bool(0))  # <type 'bool'>

print type("python")  # <type 'str'>

print type(12.12)  # <type 'float'>
print type(12.12j)  # <type 'complex'>
print type(12l + 12.12j)  # <type 'complex'>

print type(())
print type([])
print type({})


def myFunction():
    pass


print type(myFunction())  # <type 'NoneType'>


def myFunciton1():
    return 1


print type(myFunciton1())  # <type 'int'>

print type(type(1))  # <type 'type'>
