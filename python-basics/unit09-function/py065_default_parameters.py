#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午9:51
# @Author  : Aries
# @Site    : 
# @File    : py065_default_parameters.py
# @Software: PyCharm
'''
默认参数 default parameters
    1.使用默认参数的理由
        提升健壮性,其补充了标准位置参数没有提供的一些灵活性
'''


def taxMe(cost, rate=0.0825):
    return cost + cost * rate


print taxMe(100)  # 108.25


# 求圆的面积是一个很直观的例子,因为π基本属于默认值3.14159,所以作为默认参数合情合理
def get_area_circle(r, pi=3.14):
    return pi * (r ** 2)


print get_area_circle(50)  # 7850.0
print '-' * 50

# 以前的例子
def net_conn(host, port=80, stype='tcp'):
    pass
