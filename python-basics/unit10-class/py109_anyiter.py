#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/21 下午12:27
# @Author  : Aries
# @Site    : 
# @File    : py109_anyiter.py
# @Software: PyCharm
'''
任意项迭代器

'''


class AnyIter(object):
    def __init__(self, data, safe=False):
        self.safe = safe
        self.iter = iter(data)

    def __iter__(self):
        return self

    def next(self, howmany=1):
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.next())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval


if __name__ == '__main__':
    a = AnyIter(range(10))
    i = iter(a)
    for j in range(1, 5):
        print j, ':', i.next(j)

    '''
    1 : [0]
    2 : [1, 2]
    3 : [3, 4, 5]
    4 : [6, 7, 8, 9]   
    '''
