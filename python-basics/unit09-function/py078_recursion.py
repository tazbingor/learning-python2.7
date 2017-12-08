#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 上午10:29
# @Author  : Aries
# @Site    : 
# @File    : py078_recursion.py
# @Software: PyCharm
'''
递归
 函数直接或间接的调用自己,即为递归

'''


# 阶乘
def fact(n):
    print n
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print fact(5)
print '-' * 50


# 斐波那契数列 f(n) = f(n-1) + f(n-2)
def fibonacci_seq(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_seq(n - 1) + fibonacci_seq(n - 2)


print fibonacci_seq(5)
print '-' * 50

# 使用字典优化斐波那契数列
d = {0: 0, 1: 1}


def fibseq_dict(n):
    if not n in d:
        d[n] = fibseq_dict(n - 1) + fibseq_dict(n - 2)
    # print d
    return d[n]


print fibseq_dict(5)
