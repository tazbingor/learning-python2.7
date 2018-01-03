#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/3 下午6:54
# @Author  : Aries
# @Site    : 
# @File    : py140_math_sqrt_evo.py
# @Software: PyCharm
'''
10-9 改进math.sqrt() 使其能处理负数
'''
import math, cmath


def sqrt(num):
    return abs(num) ** 0.5


def sqrt_evo(num):
    try:
        result = math.sqrt(num)
    except ValueError:
        result = cmath.sqrt(num)
    return result


if __name__ == '__main__':
    print sqrt_evo(-16)  # 4j
    print sqrt_evo(16)  # 4.0

    print sqrt(-16)  # 4.0
