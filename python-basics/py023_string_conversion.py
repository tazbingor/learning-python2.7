#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/9 上午11:58
# @Author  : Aries
# @Site    : 
# @File    : py023_string_conversion.py
# @Software: PyCharm
'''
字符串转换

'''
str1 = "ABC"
str2 = u"ABC"
print str1
print str2
print str1.encode("UTF-8")
print unicode(str1, "UTF-8")

print r'\n\t嘻\t嘻'  # 不使用转义符

print isinstance(str1, unicode)
print isinstance(str2, unicode)  # True
print isinstance("woodz", str)  # True
