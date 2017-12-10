#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/17 下午8:02
# @Author  : Aries
# @Site    : 
# @File    : py047_my_pop.py
# @Software: PyCharm
'''
mypop()
'''


def myPop(temp_list):
    del temp_list[-1]
    return temp_list


list1 = ['1', '2', '3', 'pop']
print myPop(list1)
