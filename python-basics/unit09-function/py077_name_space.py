#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 上午10:22
# @Author  : Aries
# @Site    : 
# @File    : py077_name_space.py
# @Software: PyCharm
'''
名称空间

'''

j, k = 1, 2


def proc1():
    j, k = 3, 4
    print 'j==%d and k==%d' % (j, k)
    k = 5


def proc2():
    j = 6
    proc1()
    print 'j==%d and k==%d' % (j, k)


k = 7
proc1()
print 'j==%d and k==%d' % (j, k)

j = 8
proc2()
print 'j==%d and k==%d' % (j, k)
