#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 下午4:46
# @Author  : Aries
# @Site    : 
# @File    : py067_perfect_number.py
# @Software: PyCharm
'''
8-7.完全数
'''


# 获取因数
def getFactor(number):
    fList = [1]
    for i in range(1, number + 1):
        if number % 2 == 0:
            fList.append(2)
            number = number / 2
        else:
            fList.append(number)
            break
    return fList


def isPerfect(num):
    if sum(getFactor(num)) == num:
        return 1
    else:
        return 0


print isPerfect(6)
