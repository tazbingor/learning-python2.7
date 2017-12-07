#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/7 下午4:58
# @Author  : Aries
# @Site    : 
# @File    : py068_lambda.py
# @Software: PyCharm
'''
函数式编程
匿名函数和lambda

'''


# 原始的函数
def TRUE():
    return True


# lambda
result = lambda: True
print result  # <function <lambda> at 0x1079490c8>
print type(result)  # <type 'function'>
print result()  # True
print type(result())  # <type 'bool'>


# 带有默认参数
def usuallyAdd2(x, y=2):
    return x + y


print usuallyAdd2(2, 2)  # 4

usuaAdd2 = lambda x, y=2: x + y
print usuaAdd2(2, 2)  # 4


# 带有可变参数
def showAllAsTuple(*z):
    return z


print showAllAsTuple(1, 2, 3)  # (1, 2, 3)

showArgsTuple = lambda *z: z
print showArgsTuple('1', '2', '3')  # ('1', '2', '3')
