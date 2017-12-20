#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/20 下午11:07
# @Author  : Aries
# @Site    : 
# @File    : py102_multiple_inheritance.py
# @Software: PyCharm
'''
多重继承
'''


# 简单的属性查找
class P1:
    def foo(self):
        print 'p1 - foo()'


class P2:
    def foo(self):
        print 'p2 - foo()'

    def bar(self):
        print 'p2 - bar()'


class C1(P1, P2):
    pass


class C2(P1, P2):
    def bar(self):
        print 'C2 - bar()'


class GC(C1, C2):
    pass
