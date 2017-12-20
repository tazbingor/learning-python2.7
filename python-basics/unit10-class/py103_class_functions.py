#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/20 下午11:22
# @Author  : Aries
# @Site    : 
# @File    : py103_class_functions.py
# @Software: PyCharm
'''
类的内建函数
'''


class A:
    pass


class B(A):
    pass


class C1(object): pass


class C2(object): pass


if __name__ == '__main__':
    # issubclass() 判断一个类是否是另一个类的子类
    print issubclass(B, A)  # True

    # isinstance() 判断一个对象是否是另一个对象的实例
    a = A()
    b = B()
    print isinstance(a, A)
    print isinstance(b, A)
    print'-' * 50
    c1 = C1()
    c2 = C2()
    print isinstance(c1, C1)
    print isinstance(c2, C1)  # False
    print isinstance(c1, C2)  # False
    print isinstance(c2, C2)
