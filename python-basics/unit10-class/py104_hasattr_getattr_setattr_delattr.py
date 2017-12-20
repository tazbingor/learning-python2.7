#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/20 下午11:33
# @Author  : Aries
# @Site    : 
# @File    : py104_hasattr_getattr_setattr_delattr.py
# @Software: PyCharm
'''
attr系列函数在py中的工作及其频繁,特别在对类的操作时

hasattr() :判断一个对象是否有一个特定的属性,一般用于访问前的检查
getattr() :获得对象的属性,若不存在则引发异常
setattr() :为对象添加一个新属性
delattr() :删除其中一个属性
'''


class MyClass(object):
    def __init__(self):
        self.foo = 100


if __name__ == '__main__':
    myInst = MyClass()
    print hasattr(myInst, 'foo')  # True
    print getattr(myInst, 'foo')  # 100
    print hasattr(myInst, 'bar')  # False
    # print getattr(myInst, 'bar') # AttributeError: 'MyClass' object has no attribute 'bar'

    setattr(myInst, 'bar', 'my attr')
    print dir(myInst)
    delattr(myInst, 'foo')
    print dir(myInst)
