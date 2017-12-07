#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/7 下午8:06
# @Author  : Aries
# @Site    : 
# @File    : py072_scope.py
# @Software: PyCharm
'''
作用域

 搜索标识符(变量):
    当搜索一个标识符时,Python先从局部作用域开始搜索.如果在局部作用域内没有找到,那么一定会在全局找到这个变量,否则就会抛出NameError的异常
 一个变量的作用域和它寄住的命名空间相关联
'''

# globa 语句

# def foo():
#     print '\ncalling foo()'
#     bar = 200
#     print '\n foo().bar ', bar
#
#
# bar = 100
# print 'in main(),bar is', bar  # 100
# foo()  # 200
# print 'in main(),bar is', bar  # 100
is_this_global = 'xyz'


def foo():
    global is_this_global
    this_is_local = 'orz'
    is_this_global = 'wow'
    print this_is_local + is_this_global


foo()  # orzwow
print is_this_global  # wow
