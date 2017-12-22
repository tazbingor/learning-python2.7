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

