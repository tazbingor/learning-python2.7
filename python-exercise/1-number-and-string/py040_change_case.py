#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/16 下午11:07
# @Author  : Aries
# @Site    : 
# @File    : py040_change_case.py
# @Software: PyCharm
'''
字符串大小写转换

字符串。写一个函数，返回一个跟输入字符串相似的字符串，要求字符串的大小写反转
比如，输入“Mr.Ed”，应该返回“mR.eD”作为输出。
'''
str_list = list('Mr.Ed')
temp = []
print str_list
for i in str_list:
    if str(i).islower():
        temp.append(str(i).upper())
    else:
        temp.append(str(i).lower())

print ''.join(temp)
