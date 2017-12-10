#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/19 下午9:48
# @Author  : Aries
# @Site    : 
# @File    : py052_build_dictionary.py
# @Software: PyCharm
'''
创建字典
建立字典。给定两个长度相同的列表，比如说，列表[1, 2, 3,...]和['abc', 'def','ghi',...],用这两个列表里的所有数据组成一个字典，
像这样：{1:'abc', 2: 'def', 3: 'ghi',...}
'''
key_list = [1, 2, 3, 4, 5, 6]
value_list = ['Java', 'Python', 'C/C++', 'JavaScript', 'Golang', 'PHP']
dict1 = {}
for item in range(len(key_list)):
    dict1.update(dict({key_list[item]: value_list[item]}))
print dict1
