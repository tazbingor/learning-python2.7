#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/13 下午 10:29
# @Author  : Aries
# @Site    : 
# @File    : py092_instance.py
# @Software: PyCharm
'''
实例
    通过调用类来创建实例


'''


class MyClass(object):
    def show_class(self):
        print 'this is \'MyClass\''


class MyClass01(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __new__(cls, *args, **kwargs):
        pass

    def __del__(self):
        pass


if __name__ == '__main__':
    mc = MyClass()
    mc.show_class()  # this is 'MyClass'
