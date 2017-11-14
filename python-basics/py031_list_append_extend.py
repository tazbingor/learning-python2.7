#!/usr/bin/env python
# coding: utf-8
# -*- coding: utf-8 -*-
# @Time    : 17/11/14 下午5:20
# @Author  : Aries
# @Site    : 
# @File    : py031_list_append_extend.py
# @Software: PyCharm
import sys

reload(sys)
sys.setdefaultencoding('utf8')
'''
list 内建函数 append 追加 和 extend 扩展

主要区别
1. append和extend都仅只可以接收一个参数，
2. append 添加任意obj, 追加新的元素,将obj以一个整体的形式添加到list末尾,并占一个元素位(类似于打包的效果)
3. extend 添加任意obj, 扩展新的元素,将obj中的一个或者是多个元素逐一添加至原有list当中

ps: py2.2之前,extend只能添加列表
'''

test_list1 = ['A', 'B', 'C', 'D']
test_list2 = ['E', 'F', 'G', 'H']
test_list1.append(test_list2)
print test_list1  # ['A', 'B', 'C', 'D', ['E', 'F', 'G', 'H']]
test_list3 = ('I', 'J', 'K')
test_list2.append(test_list3)  # ['E', 'F', 'G', 'H', ('I', 'J', 'K')]
print test_list2
print

arr1 = ['1', '2', '3']
arr2 = ['7', '8', '9']
arr1.extend(arr2)
print arr1  # ['1', '2', '3', '7', '8', '9']
arr3 = ('4', '5', '6')
arr1.extend(arr3)
print arr1  # ['1', '2', '3', '7', '8', '9', '4', '5', '6']
