#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 下午2:59
# @Author  : Aries
# @Site    : 
# @File    : py065_factor.py
# @Software: PyCharm
'''
8.5 约数. 完成一个名为getfactors()的函数.它接受一个整型作为参数,返回它所有约数的
   列表,包括1和它本身.
'''


def getFactors(number):
    fList = [1, number]
    for i in range(1, number + 1):
        if number % 2 == 0:
            fList.append(2)
            number = number / 2
        else:
            fList.append(number)
            break
    return fList


print getFactors(100)
