#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 上午11:57
# @Author  : Aries
# @Site    : 
# @File    : py014_nested_list_sum.py
# @Software: PyCharm
'''
递归:嵌套列表求和

'''


def nested_list_sum(numList):
    sum = 0
    for eachItem in numList:
        if isinstance(eachItem, list):
            sum += nested_list_sum(eachItem)
        else:
            sum += eachItem
    return sum


list1 = [1, 2, 3, [1, 2, 3], [[2, 4], 5], [1, 2, [5, 4]]]
print nested_list_sum(list1)
