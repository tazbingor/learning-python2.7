#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/15 上午6:00
# @Author  : Aries
# @Site    : 
# @File    : py097_staticmethod_and_classmethod.py
# @Software: PyCharm
'''
静态方法和类方法

'''


class TestStaticMethod:
    def foo():
        print '这是静态函数foo'

    foo = staticmethod(foo)


class TestClassMethod:
    def foo(cls):
        print '这是类函数foo'
        print'所属于', cls.__name__

    foo = classmethod(foo)


# 利用函数修饰符来修饰函数
class TestStaticMethod_01:
    @staticmethod
    def foo():
        print '这是函数修饰符 @staticmethod 所修饰的静态函数foo'


class TestClassMethod_01:
    @classmethod
    def foo(cls):
        print '这是函数修饰符 @staticmethod 所修饰的静态函数foo'
        print 'foo() 所属于:', cls.__name__


if __name__ == '__main__':
    tsm = TestStaticMethod()
    TestStaticMethod.foo()
    tsm.foo()
    print '-' * 50
    tcm = TestClassMethod()
    TestClassMethod.foo()
    tcm.foo()
    print '-' * 50

    tsm1 = TestStaticMethod_01()
    TestStaticMethod_01.foo()
    tsm1.foo()
    print '-' * 50
    tcm1 = TestClassMethod_01()
    TestClassMethod_01.foo()
    tcm1.foo()
