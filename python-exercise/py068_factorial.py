#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 下午5:00
# @Author  : Aries
# @Site    : 
# @File    : py068_factorial.py
# @Software: PyCharm
'''
8-8.阶乘. 一个数的阶乘被定义为从1到该数字所有数字的乘积.
N的阶乘简写为N!. N! == factorial(N) == 1*2*3...(N-2)*(N-1)*N,所以, 4! == 1 * 2 * 3 * 4,写一个函数,指定N,返回N!的值.
'''

def factorial(number):
    if number == 0 and number == 1:
        return 1
    total = 1
    for i in range(2, number + 1):
        total *= i
    return total


print factorial(4)
