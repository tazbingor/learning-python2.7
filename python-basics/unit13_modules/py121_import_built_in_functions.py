#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/5 下午11:16
# @Author  : Aries
# @Site    : 
# @File    : py121_import_built_in_functions.py
# @Software: PyCharm
'''
模块内建函数
__import__() 导入模块函数
globals() 返回全局名称空间的字典
locals() 返回局部名称空间的字典

'''


def foo():
    print '\n calling foo()..'
    string = 'bar'
    anInt = 42
    print 'foo()\'s globals:', globals().keys()
    print 'foo()\'s locals::', locals().keys()


if __name__ == '__main__':
    sys = __import__('sys')
    print sys  # <module 'sys' (built-in)>
    print '-' * 50
    print 'main\'s globals:', globals().keys()
    # main's globals: ['__builtins__', '__file__', '__package__', 'sys', '__name__', 'foo', '__doc__']

    print 'main\'s locals::', locals().keys()
    # main's locals:: ['__builtins__', '__file__', '__package__', 'sys', '__name__', 'foo', '__doc__']

    foo()
    '''
     calling foo()..
    foo()'s globals: ['__builtins__', '__file__', '__package__', 'sys', '__name__', 'foo', '__doc__']
    foo()'s locals:: ['anInt', 'string']
    '''
