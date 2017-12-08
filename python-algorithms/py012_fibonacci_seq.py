#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 上午10:58
# @Author  : Aries
# @Site    : 
# @File    : py012_fibonacci_seq.py
# @Software: PyCharm
'''
python实现斐波那契数列
'''


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
