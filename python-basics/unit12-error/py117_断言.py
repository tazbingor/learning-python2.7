#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/2 下午8:06
# @Author  : Aries
# @Site    : 
# @File    : py117_断言.py
# @Software: PyCharm
'''
assert 断言
'''


def division(num1, num2):
    assert num2 != 0
    return num1 // num2


# assert 断言的实现
def test_assert(expr, args=None):
    if __debug__ and not expr:
        raise AssertionError, args


if __name__ == '__main__':
    # print division(1, 0) # AssertionError
    print division(18, 2)  # 9


