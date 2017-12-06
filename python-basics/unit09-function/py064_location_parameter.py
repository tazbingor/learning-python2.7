#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午9:45
# @Author  : Aries
# @Site    : 
# @File    : py064_location_parameter.py
# @Software: PyCharm
'''
位置参数  location parameter
    位置参数必须以在被调用的参数中定义的准确顺序来传递.另外,没有任何默认参数的情况下,传入参数的数目必须以声明的数字一致
'''


def foo(who):
    print 'hello', who


def main():
    foo('tazdingo bean')  # hello tazdingo bean


if __name__ == '__main__':
    main()
