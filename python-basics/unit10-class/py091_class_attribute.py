#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/13 下午 09:59
# @Author  : Aries
# @Site    : 
# @File    : py091_class_attribute.py.py
# @Software: PyCharm

'''
类属性
    python严格要求，类没有实例化，其中的方法是不能被调用的！
  这种行为叫做绑定，方法必须绑定在一个实例上

决定类的属性
    __name__
    __dict__


'''


class C(object):
    foo = 100


class MyClass(object):
    def myNoActionMehod(self):
        print '这是类的引用'


class MyClass01(object):
    my_version = '7.35'  # 静态数据

    def show_my_version(self):
        print MyClass01.my_version


if __name__ == '__main__':
    # 简单引用类属性
    print C.foo  # 100
    C.foo += 1
    print C.foo  # 101

    # 简单引用类
    my_class = MyClass()
    my_class.myNoActionMehod()

    # 使用dir和__dict__查看类的属性
    print dir(MyClass01)
    print '-' * 50
    print MyClass01.__dict__
    # 其他特殊属性
    print MyClass01.__name__  # MyClass01
    print MyClass01.__doc__  # None
    print MyClass01.__bases__  # (<type 'object'>,)
    print MyClass01.__module__  # __main__
    print MyClass01.__class__  # <type 'type'>
