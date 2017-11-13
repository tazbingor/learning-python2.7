#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/9 下午10:14
# @Author  : Aries
# @Site    : 
# @File    : py025_string_functions.py
# @Software: PyCharm
import string

'''
python string 内建函数
'''

# 输出0-9
print string.digits
print type(string.digits)

# 输出小写的a-z
print string.lowercase
print type(string.lowercase)

# 输出空格符
print string.whitespace
print len(string.whitespace)  # 长度为6
print type(string.whitespace)

# 首字母大写
str1 = 'hello'
print str1.capitalize()  # Hello
print
# 返回一个居中的字符串,字符前后填充总数为width的空格,也可自定义填充其他字符
str2 = 'rich'
str2.center(4, '*')

print str2
print len(str2)
print