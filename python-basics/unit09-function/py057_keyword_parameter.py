#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午7:15
# @Author  : Aries
# @Site    : 
# @File    : py057_keyword_parameter.py
# @Software: PyCharm
'''
关键字参数
    1. 当调用函数,没有函数参数的时候,可以使用关键字参数.者取决于函数的默认参数
'''


def test_add(x=4, y=4):
    return x + y


if __name__ == '__main__':
    # 没有参数时,
    print test_add()  # 8
    # 有参数时
    print test_add(8, 8)  # 16
