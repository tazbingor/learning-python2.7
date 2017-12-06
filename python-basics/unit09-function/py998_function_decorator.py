#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午8:44
# @Author  : Aries
# @Site    :
# @File    : py998_function_decorator.py
# @Software: PyCharm
'''
函数装饰器 function decorator

装饰器的定义是：装饰器实质上是一个函数。它把一个函数作为输入并且返回另外一个函数。其实其是闭包概念的深化。

'''


def eat(func):
    def apple():
        print 'apple'

    func()


def jujube():
    print 'jujube'


if __name__ == '__main__':
    eat(jujube)
