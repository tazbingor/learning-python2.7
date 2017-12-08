#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午1:58
# @Author  : Aries
# @Site    : 
# @File    : py084_generator.py
# @Software: PyCharm
'''
生成器
 1. 生成器就是一种迭代器。
 2. 生成器也具有next(),自动迭代
 3. 自带yield功能,状态挂起
'''

# 生成器表达式
g = (i for i in range(6))
print g  # <generator object <genexpr> at 0x10e2dab40>
print type(g)  # <type 'generator'>
print g.next()  # 0
print g.next()  # 1
print g.next()  # 2
print g.next()  # 3
print g.next()  # 4
print g.next()  # 5
print '-' * 50


# 使用生成器写一个返回自然数的平方的函数

def gensquares(n):
    for item in range(n):
        yield item ** 2


for item in gensquares(5):
    print item,  # 0 1 4 9 16

# def get_BMI_value(kg, m):
#     return float(kg / m ** 2)
#
#
# print get_BMI_value(97, 1.81)
