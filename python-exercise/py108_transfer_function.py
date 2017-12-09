#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午11:17
# @Author  : Aries
# @Site    : 
# @File    : py108_transfer_function.py
# @Software: PyCharm
'''
11–12. 传递函数。
给在这章中描述的testit()函数写一个姊妹函数。
timeit()会带一个函数对象（和参数一起）以及计算出用了多少时间来执行这个函数，而不是测试执行时的错误。
返回下面的状态：函数返回值，消耗的时间。你可以用time.clock()或者time.time()，无论哪一个给你提供了较高的精度。
（一般的共识是在POSIX 上用time.time()，在win32 系统上用time.clock()）
注意：timeit()函数与timeit 模块不相关(在python2.3 中引入）
'''

import time


def timeit(func, *nkwargs, **kwargs):
    # type: (function, object, object) -> object
    try:
        start = time.clock()
        retval = func(*nkwargs, **kwargs)
        end = time.clock()
        result = (True, retval, end - start)
    except Exception, diag:
        result = (False, str(diag))
    return result


def main():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')
    for eachFunc in funcs:
        print '-' * 80
        for eachVal in vals:
            retval = timeit(eachFunc, eachVal)
            if retval[0]:
                print '%s(%s)=' % (eachFunc.__name__, eachVal), retval[1],
                print 'this func cost %s secs' % retval[2]
            else:
                print '%s(%s)=FAILED: ' % (eachFunc.__name__, eachVal), retval[1]


if __name__ == '__main__':
    main()
