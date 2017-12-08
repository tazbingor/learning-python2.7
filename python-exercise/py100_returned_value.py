#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午4:48
# @Author  : Aries
# @Site    : 
# @File    : py100_returned_value.py
# @Software: PyCharm
'''
11–4. 返回值。
给你在5-13 的解创建一个补充函数。创建一个带以分为单位的总时间以及返回一个以小时和分为单位的等价的总时间。

'''


def getTime(min):
    return '%sh:%sm' % (min / 60, min % 60)


def main():
    print getTime(280)
    print getTime(180)


if __name__ == '__main__':
    main()
