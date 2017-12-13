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
    def __init__(self):
        print '__init__先调用'

    # new 先于init执行
    def __new__(cls, *args, **kwargs):
        print '__new__先调用'

    def __del__(self):
        print '__del__先调用'


if __name__ == '__main__':
    mc = MyClass()
    mc.show_class()  # this is 'MyClass'
    print '-' * 50
    mc1 = MyClass01()  # __new__先调用
