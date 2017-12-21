#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/21 下午12:21
# @Author  : Aries
# @Site    : 
# @File    : py108_RandSeq.py
# @Software: PyCharm
'''
随机顺序迭代器
'''
from random import choice


class RandSeq(object):
    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        return self

    def next(self):
        return choice(self.data)


def main():
    for eachItem in RandSeq(
            ('rock', 'paper', 'scissors')):
        print eachItem


if __name__ == '__main__':
    main()
