#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/7 下午10:21
# @Author  : Aries
# @Site    : 
# @File    : py074_closure_02.py
# @Software: PyCharm
'''
追踪闭包变量
'''

output = '<int %r id=%#0x val=%d>'
w = x = y = z = 1


# 因为此处的x,y,z是局部变量,并未修改外部变量,不构成闭包的条件
def f1():
    x = y = z = 2


def f2():
    y = z = 3

    def f3():
        z = 4
        print output % ('w', id(w), w)
        print output % ('x', id(x), x)
        print output % ('y', id(y), y)
        print output % ('z', id(z), z)

    clo = f3.func_closure
    if clo:
        print 'f3 closure vars:', [str(c) for c in clo]
    else:
        print 'no f3 closure vars'

    f3()

    clo = f2.func_closure
    if clo:
        print 'f2 closure vars:', [str(c) for c in clo]
    else:
        print 'no f2 closure vars'
    f2()


clo = f1.func_closure
if clo:
    print 'f1 closure vars:', [str(c) for c in clo]
else:
    print 'no f1 closure vars'
f1()
