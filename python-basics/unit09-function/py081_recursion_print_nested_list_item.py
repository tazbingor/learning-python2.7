#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午12:06
# @Author  : Aries
# @Site    : 
# @File    : py081_recursion_print_nested_list_item.py
# @Software: PyCharm
'''
递归:打印嵌套列表中的所有元素
'''


def print_nested_list(strList):
    for eachItem in strList:
        if isinstance(eachItem, list):
            print_nested_list(eachItem)
        else:
            print eachItem


list1 = ['python', ['js', 'ts', 'cs'], ['scheme', 'common lisp']]
print_nested_list(list1)
