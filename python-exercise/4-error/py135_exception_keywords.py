#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/3 下午5:48
# @Author  : Aries
# @Site    : 
# @File    : py135_exception_keywords.py
# @Software: PyCharm
'''
10-3 引发异常的关键字有哪些?
    raise

10-4 关键字,try-except 和try-finally 有什么不同?

'''


def test1(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print '运算异常:除数不能为0'


def test2(num1, num2):
    try:
        return num1 / num2
    finally:
        return num1 / num1


if __name__ == '__main__':
    test1(1, 0)  # 运算异常:除数不能为0
    print test2(1, 0)  # 1
'''
从上述两个例子中就能很明显的看出
try-except,倘若执行try中代码出现了异常,那么except下的语句必然执行,反之亦然
try-finally,无论try中是否出现异常,finally下的代码必然执行
'''
