#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/7 下午4:30
# @Author  : Aries
# @Site    : 
# @File    : py067_variable_arity_methods.py
# @Software: PyCharm
'''
可变长度参数
    包含:
    1.非关键字可变长参数(元组)
    2.关键字变量参数(字典)
'''


# 非关键字参数
def tupleVarArgs(arg1, arg2='defaultB', *theRest):
    print 'from arg 1:', arg1
    print 'from arg 2:', arg2
    for eachXtrArg in theRest:
        print 'another arg:', eachXtrArg


# 关键字参数
def dictVarArgs(arg1, arg2='defaultB', **theRest):
    print 'from arg 1:', arg1
    print 'from arg 2:', arg2
    for eachXtrArg in theRest.keys():
        print 'Xtr arg %s: %s' % (eachXtrArg, str(theRest[eachXtrArg]))


# 关键字参数和非关键字参数
def newFoo(arg1, arg2, *nkw, **kw):
    print 'from arg 1:', arg1
    print 'from arg 2:', arg2
    for eachNkw in nkw:
        print 'another arg:', eachNkw
    for eachKw in kw:
        print 'nkw %s : %s' % (eachKw, str(kw[eachKw]))


if __name__ == '__main__':
    # tuple
    tupleVarArgs('abc')
    print '-' * 50
    tupleVarArgs(23, 4.56)
    print'-' * 50
    tupleVarArgs('abc', 123, 'xyz', 456.789)
    print'-' * 50

    # dict
    dictVarArgs(1220, 740.0, c='grail')
    print'-' * 50
    dictVarArgs(arg2='tales', c=123, d='poe', arg1='mystery')
    print'-' * 50
    dictVarArgs('one', d=10, e='zoo', men=('freud', 'gaudi'))
    print'-' * 50

    # t&d
    newFoo('wolf', 3, 'projects', freud=90, gamble=96)
