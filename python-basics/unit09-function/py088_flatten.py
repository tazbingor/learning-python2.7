#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午3:17
# @Author  : Aries
# @Site    : 
# @File    : py088_flatten.py
# @Software: PyCharm
'''
生成器实现列表降维
也可使用相同方法实现dict降维
'''

numList = [1, 2, [3, 4, [5, 6], [7, 8, [9, 10]], 11], 12]

def flatten(alist):
    for eachItem in alist:
        if isinstance(eachItem, list):
            for i in flatten(eachItem):
                yield i
        else:
            yield eachItem

if __name__ == '__main__':
    print numList
    print list(flatten(numList))
