#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/20 下午11:49
# @Author  : Aries
# @Site    : 
# @File    : alg001_concept.py
# @Software: PyCharm
'''
倘若a+b+c = 1000,且a^2+b^2=c^2 (a,b,c为自然数)
    求出a,b,c可能的组合

最简单的解法,巨慢无比!
'''
import time


def get_combination():
    start_time = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            for c in range(0, 1001):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print 'a,b,c:%d,%d,%d' % (a, b, c)
    end_time = time.time()
    print 'times:%d' % (end_time - start_time)
    print 'finished'


if __name__ == '__main__':
    get_combination()
    '''
    a,b,c:0,500,500
    a,b,c:200,375,425
    a,b,c:375,200,425
    a,b,c:500,0,500
    times:67
    finished
    '''
