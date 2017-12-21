#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/21 上午11:03
# @Author  : Aries
# @Site    : 
# @File    : py105_customization.py
# @Software: PyCharm
'''
简单定制
'''


class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), \
            'VALUE must be a float!'
        self.value = round(val, 2)


if __name__ == '__main__':
    # rfm = RoundFloatManual(60)  # AssertionError: VALUE must be a float!
    rfm1 = RoundFloatManual(7.35)
    # print round(7.35, 2)
    print rfm1.value
