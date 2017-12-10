#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/15 上午3:59
# @Author  : Aries
# @Site    : 
# @File    : py032_Identification_string.py
# @Software: PyCharm
'''
练习 6 -1
鉴定字符串,在string模块中是否有方法鉴定下一个字符串是上一个字符串的一部分?

'''
import string

# 使用in
str1 = 'public static void main'
str2 = 'static'
print str2 in str1  # True

# 使用string.count 显示str2存在str1中的次数
print str1.count(str2)  # 1 次

# 使用find()方法 若存在,则返回的是索引开始的位置
print str1.find(str2)  # 7

# index()与find()类型,若不包含则出现异常信息
print str1.index(str2)  # 7

# rfind(), 和find()类似,是逆向查找
print str1.rfind(str2)  # 7

# rindex(), 逆向查找的index()
print str1.rfind(str2)  # 7
