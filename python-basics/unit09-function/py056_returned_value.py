#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午6:58
# @Author  : Aries
# @Site    : 
# @File    : py056_returned_value.py
# @Software: PyCharm
'''
函数返回值
    1. 在python中,函数没有返回值,那么其默认函数返回值为None,这是解析器的判断.相当于java中给方法声明返回值类型的void
    2. python中的函数可以返回一个值或者对象

'''


def hello():
    print 'hello world'


hello_hi = hello()


def bar():
    return ('abc', 'Java', 'Python')


if __name__ == '__main__':
    hello()  # TypeError: 'NoneType' object is not callable
    hello_hi

    print type(hello_hi)
    print hello_hi
    print  '-' * 50
    # 若返回值是元组,如何储存
    # 一下三种储存返回值的方式为等价
    aTuple = bar()
    x, y, z = bar()
    (a, b, c) = bar()
    print aTuple
    print x, y, z # 会被拆分为单独的变量
    print (a, b, c)
