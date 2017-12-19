#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/19 下午3:29
# @Author  : Aries
# @Site    : 
# @File    : py099_Inheritance_overlay_method.py
# @Software: PyCharm
'''
通过继承覆盖方法
super不但能找到基类方法,还可以调用self
'''


class P(object):
    def foo(self):
        print '我是class P中的foo()'


class C(P):
    def foo(self):
        print '我是class C中的foo()'


class S(P):
    def foo(self):
        super(S, self).foo()
        print '我是class S的foo()'


if __name__ == '__main__':
    p = P()
    p.foo()  # 我是class P中的foo()

    c = C()
    c.foo()  # 我是class C中的foo()

    s = S()
    s.foo()  # 我是class P中的foo()
    # 我是class S的foo()
