#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午6:11
# @Author  : Aries
# @Site    : 
# @File    : py105_functional_reduce.py
# @Software: PyCharm
'''
11–9. 用reduce()进行函数式编程。
复习11.7.2 部分，阐述如何用reduce()数字集合的累加的代码。修改它，创建一个叫average()的函数来计算每个数字集合的简单的平均值。
'''
average = lambda num: reduce((lambda a, b: a + b), range(num)) // len(range(num))
if __name__ == '__main__':
    print average(10)  # 4
    print average(5)  # 2
