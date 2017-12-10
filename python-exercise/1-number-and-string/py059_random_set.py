#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/20 下午9:07
# @Author  : Aries
# @Site    : 
# @File    : py059_random_set.py
# @Software: PyCharm
'''
随机数。
修改练习5-7的代码，用random中的randint()或者randrange()生成一个随机数集合，
从0-9（包括9）中随机选择1到10个随机数，然后组成一个集合A，同理生成B，然后显示A|B 和 A&B。

'''

import random


def getSetUnion(set1, set2):
    return set1 | set2


def getSetIntersect(set1, set2):
    return set1 & set2


def getRandomSet():
    rs = set()
    for i in range(random.randint(1, 10)):
        rs.add(random.randint(0, 9))
    return rs


random_set1 = getRandomSet()
random_set2 = getRandomSet()
print random_set1
print random_set2
print getSetUnion(random_set1, random_set2)
print getSetIntersect(random_set1, random_set2)
