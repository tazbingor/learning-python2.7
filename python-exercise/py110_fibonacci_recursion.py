#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/9 上午8:41
# @Author  : Aries
# @Site    : 
# @File    : py110_fibonacci_recursion.py
# @Software: PyCharm
'''
11–14. 递归。
我们也来看下在第八章中的Fibonacci 数字。重写你先前计算Fibonacci 数字的解(练习8-9）以便你可以使用递归。
'''


def fibonacci_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


# 优化版
template = {0: 0, 1: 1}


def fibonacci_recursion_plus(n):
    if not n in template:
        template[n] = fibonacci_recursion_plus(n - 1) + fibonacci_recursion_plus(n - 2)
    return template[n]


def main():
    print fibonacci_recursion(5)  # 5
    print fibonacci_recursion(6)  # 8
    print '-' * 50
    print fibonacci_recursion_plus(5)  # 5
    print fibonacci_recursion_plus(6)  # 8


if __name__ == '__main__':
    main()
