#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/8 下午6:01
# @Author  : Aries
# @Site    : 
# @File    : py031_is_and_equal.py
# @Software: PyCharm
'''
解释"is "和"= ="之间的差异,举例说明,对is 返回为假,= = 返回为真。

首先"=="是比较操作符,是用来比较值是否相等

而"is"在python中表示同一性运算符,比较的是对象的唯一id


'''

str1 = '12'
str2 = str(12)

print str1 is str2
print str1 == str2

print id(str1) == id(str2)
