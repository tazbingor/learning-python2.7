#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/21 上午11:33
# @Author  : Aries
# @Site    : 
# @File    : py106_basic_customization.py
# @Software: PyCharm
'''
基本定制
'''


class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), \
            'Value must be a float!'
        self.value = round(val, 2)

    def __str__(self):
        return '%.2f' % self.value

    __repr__ = __str__


def main():
    rfm = RoundFloatManual(1.121)
    print rfm.value  # 1.12
    print rfm.__str__()  # 1.12
    print rfm.__repr__()  # 1.12


if __name__ == '__main__':
    main()
