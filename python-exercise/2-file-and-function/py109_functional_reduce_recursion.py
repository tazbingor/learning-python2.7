#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/9 上午8:15
# @Author  : Aries
# @Site    : 
# @File    : py109_functional_reduce_recursion.py
# @Software: PyCharm
'''
11–13.使用reduce()进行函数式编程以及递归。
在第8 张中，我们看到N 的阶乘或者N!作为从1 到N 所有数字的乘积。
(a)用一分钟写一个带x,y 并返回他们乘积的名为mult(x,y)的简单小巧的函数。
(b)用你在a 中创建mult()函数以及reduce 来计算阶乘。
(c)彻底抛弃掉mult()的使用，用lamda 表达式替代。
(d)在这章中，我们描绘了一个递归解决方案来找到N!用你在上面问题中完成的timeit()函数，并给三个版本阶乘函数计时(迭代的，reduce()以及递归）
'''
import time


# a
def mult(x, y): return x * y


# c
mult_rec = lambda x, y: x * y


# b
def factor(num, func=mult):
    return reduce(func, range(1, num + 1))


# br
factorial = lambda n: reduce(mult, range(1, n + 1))


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
    eachVal = 5
    functions = (mult_rec, factor, factorial)
    for eachFunc in functions:
        print '-' * 50
        retval = timeit(eachFunc, eachVal)
        if retval[0]:
            print '%s(%s)=' % (eachFunc.__name__, eachVal), retval[1],
            print 'this func cost %s secs' % retval[2]
        else:
            print '%s(%s)=FAILED: ' % (eachFunc.__name__, eachVal), retval[1]


if __name__ == '__main__':
    main()
