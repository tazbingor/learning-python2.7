#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午2:38
# @Author  : Aries
# @Site    : 
# @File    : py085_generator_fibonacci_seq.py
# @Software: PyCharm
'''
生成器实现斐波那契数列
'''


def fib_seq_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fib_seq = fib_seq_generator()
print [fib_seq.next() for item in range(10)]
