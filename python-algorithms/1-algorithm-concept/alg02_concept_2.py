#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/20 下午11:58
# @Author  : Aries
# @Site    : 
# @File    : alg02_concept_2.py
# @Software: PyCharm
'''
优化版
倘若a+b+c = 1000,且a^2+b^2=c^2 (a,b,c为自然数)
    求出a,b,c可能的组合

time complexity 时间复杂度
    假设存在函数g，使得算法A处理规模为n的问题示例所用时间为T(n)=O(g(n))，
    则称O(g(n))为算法A的渐近时间复杂度，简称时间复杂度，记为T(n)

'''
import time


def get_combination():
    start_time = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001 - a):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print 'a,b,c:%d,%d,%d' % (a, b, c)
    end_time = time.time()
    print 'times:%d' % (end_time - start_time)
    print 'finished'


if __name__ == '__main__':
    get_combination()
    # a,b,c:0,500,500
    # a,b,c:200,375,425
    # a,b,c:375,200,425
    # a,b,c:500,0,500
    # times:0
    # finished
