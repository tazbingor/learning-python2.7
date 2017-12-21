#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/21 上午11:58
# @Author  : Aries
# @Site    : 
# @File    : py107_numerical_custom.py
# @Software: PyCharm
'''
数值定制
'''


class Time60(object):
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

    def __str__(self):
        return '%d:%d' % (self.hr, self.min)

    __repr__ = __str__

    # 加法
    def __add__(self, other):
        return self.__class__(self.hr + other.hr,
                              self.min + other.min)

    # 原位加法
    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self


if __name__ == '__main__':
    mon = Time60(10, 30)
    tue = Time60(11, 15)
    print mon + tue  # 21:45
    print mon  # 10:30
    print tue  # 11:15
