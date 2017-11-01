#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/1 下午4:41
# @Author  : Aries
# @Site    : 
# @File    : py009_standard_type.py
# @Software: PyCharm
# python标准类型
'''
数字类型
integer 整型
long integer 长整型
float 浮点型
complex number 复数型
'''
var1 = 10;  # 表示整型
var2 = 678L  # 表示长整型
var3 = 12.34;  # 表示浮点型
var4 = 123j  # 复数
var5 = 123 + 45j  # 复数

# Python字符串
str = "I love Python"

# 布尔类型
result = True

# List 列表
arr = [i for i in range(1, 10)]
print arr

# Tuple 元组
temp_list = (i for i in range(1, 10))
print temp_list

# Dictionary 字典类型
my_dict = {'巨蟒': 'Python', '咖啡': 'Java', '世间最好': 'PHP'}
print my_dict
