#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/15 上午6:59
# @Author  : Aries
# @Site    : 
# @File    : py098_inheritance.py
# @Software: PyCharm
'''
python Inheritance 继承
    一个子类可以继承他的基类的任何属性,不管是数据属性还是方法


    __bases__ 类属性
        若有,则返回相对所有的基类
        没有则返回空None
'''


class Parent:
    def __init__(self):
        print 'created an instance of', self.__class__.__name__


class Child(Parent):
    pass


class A(object):
    # def foo(self):
    #     print 'A foo()'
    pass


class B(A):
    # def zoo(self):
    #     print 'B zoo()'
    pass


class C(B):
    pass


class D(B, A):
    # def foo(self):
    #     print 'D foo()'
    pass


if __name__ == '__main__':
    p = Parent()  # 父类实例
    print p.__class__  # __main__.Parent
    # print p.__bases__  # Error

    print p.__doc__  # None

    print '-' * 50
    c = Child()
    print c.__class__  # __main__.Child
    print Child.__bases__  # (<class __main__.Parent at 0x10f8558d8>,)
    print c.__doc__  # None

    print '-' * 50

    print A.__bases__  # (<type 'object'>,)
    print B.__bases__  # (<class '__main__.A'>,)
    print C.__bases__  # (<class '__main__.B'>,)
    print D.__bases__
