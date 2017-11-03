#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/3 上午10:28
# @Author  : Aries
# @Site    : 
# @File    : py020_number_functions_integer.py
# @Software: PyCharm
'''
适用于integer的内建方法
'''

# 进制转换函数

# 八进制转换oct()
print oct(100)  # 0144
print oct(10)  # 012
print oct(1)  # 01

# 十六进制转换 hex()
print hex(100)  # 0x64
print hex(10)  # 0xa
print hex(1)  # 0x1

# ASCII 美国信息交换标准代码
# ord() 只接受一个字符,返回其对应的整型
print ord('a')  # 97
print ord('b')  # 98
print ord('c')  # 99
