#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/22 下午7:31
# @Author  : Aries
# @Site    : 
# @File    : py110_multitype_customization.py
# @Software: PyCharm
'''
多类型定制
'''


class NumberStr(object):
    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string

    def __str__(self):
        return '[%d :: %r]' % \
               (self.__num, self.__string)

    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, NumberStr):
            return self.__class__(
                self.__num + other.__num,
                self.__string + other.__string)
        else:
            raise TypeError, 'TYPE ERROR'

    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(
                self.__num * num,
                self.__string * num)
        else:
            raise TypeError, 'TYPE ERROR'

    def __nonzero__(self):
        return self.__num or len(self.__string)

    def __norm_cval(self, cmpres):
        return cmp(cmpres, 0)

    def __cmp__(self, other):
        return self.__norm_cval(cmp(self.__num, other.__num)) + \
               self.__norm_cval(cmp(self.__string, other.__string))


def main():
    a = NumberStr(3, 'foo')
    b = NumberStr(3, 'goo')
    c = NumberStr(2, 'foo')
    d = NumberStr()
    e = NumberStr(string='boo')
    f = NumberStr(1)

    print a  # [3 :: 'foo']

    print b  # [3 :: 'goo']

    print c  # [2 :: 'foo']

    print d  # [0 :: '']

    print e  # [0 :: 'boo']

    print f  # [1 :: '']

    print a < b

    print b < c  # False

    print a == a

    print b * 2  # [6 :: 'googoo']

    print a * 3  # [9 :: 'foofoofoo']

    print b + e  # [3 :: 'gooboo']

    print e + b  # [3 :: 'boogoo']


if __name__ == '__main__':
    main()
