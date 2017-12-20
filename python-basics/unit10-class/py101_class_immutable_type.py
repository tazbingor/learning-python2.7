#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/19 下午5:10
# @Author  : Aries
# @Site    : 
# @File    : py101_class_immutable_type.py
# @Software: PyCharm
'''
不可变类型
'''


class RoundFloat(float):
    def __new__(cls, val):
        return super(RoundFloat, cls).__new__(cls, round(val, 2))


if __name__ == '__main__':
    print RoundFloat(1.5955)
    print RoundFloat(1.5945)
    print RoundFloat(-1.9955)
