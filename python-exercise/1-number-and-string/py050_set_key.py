#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/19 下午6:28
# @Author  : Aries
# @Site    : 
# @File    : py050_set_key.py
# @Software: PyCharm
'''
字典的键. 我们知道字典的值可以是任意的 Python 对象,那字典的键又如何呢?
请试着将除数字和字符串以外的其他不同类型的对象作为字典的键,看一看哪些类型可以,哪些不行?

键必须是可哈希的。所有不可变的类型都是可哈希的，因此他们都可以作为字典的键。
一个要说明的问题是：值相等的数字表示相同的键。换句话说，整型数字1和浮点型1.0的哈希值是相同的，即它们是相同的键。
同时，也有一些可变对象(很少)是可哈希的，它们可以作为字典的键，但很少见。
用元组做有效的键，必须要加限制：元组中只包括像数字和字符串这样的不可变参数，才可以作为字典中有效的键。
简而言之,key必须是不可变类型
'''
# 以列表为key
# list_key_dict = {[1, 2]: 'list'}
# print list_key_dict  # TypeError: unhashable type: 'list' list不是哈希类型

# 以元组为key
tuple_key_list = {(1, 2): 'tuple'}
print tuple_key_list  # {(1, 2): 'tuple'}
print tuple_key_list.keys()  # [(1, 2)]
