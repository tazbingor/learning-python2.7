#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/7 下午8:28
# @Author  : Aries
# @Site    : 
# @File    : py073_closure.py
# @Software: PyCharm
'''
闭包
    闭包概念：
        在一个内部函数中，对外部作用域的变量进行引用，(并且一般外部函数的返回值为内部函数)，那么内部函数就被认为是闭包。
        也就是说一个持有外部环境变量的函数就是闭包。

    闭包作用：
        1.编写惰性求值的代码，保持函数调用的稳定状态。
        2.装饰器。

'''


# 简单闭包
def counter(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]

    return incr


# def cycle(func):
#     return cycle

def foo():
    x = {}
    x[0] = 5

    def inner():
        x[0] += 2
        return x[0]

    return inner


a = 10


def add():
    # global a
    return a + 10


print add()

if __name__ == '__main__':
    # count = counter(5)
    # print count()
    # add = lambda a, b: a + b
    # cycle = lambda func: cycle
    # print cycle(add(1, 2))
    p = foo()
    print p()
    print p()
    print p()
