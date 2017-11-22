#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 下午5:29
# @Author  : Aries
# @Site    : 
# @File    : py069_Fibonacci.py
# @Software: PyCharm
'''
8-9 斐波那契数列.  斐波那契数列形如1,1,2,3,5,8,13,21,等等. 也就是说,下一个值是序列
   中前两个值之和. 写一个函数,给定N,返回第N个斐波那契数字.例如,第1个斐波那契数字
   是1,第6个是8.

'''


def myFibonacci(num):
    if num <= 1:
        return num
    else:
        return myFibonacci(num - 1) + myFibonacci(num - 2)


print myFibonacci(12)  # 144
