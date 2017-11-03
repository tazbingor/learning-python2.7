#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/3 上午10:39
# @Author  : Aries
# @Site    : 
# @File    : py021_number_other.py
# @Software: PyCharm

# number的其他类型

# 布尔数 依旧需要使用 bool()函数
print bool(1)
print bool(2)
print bool(0)  # False
print bool(1.0)

# 使用布尔数
foo = 42
bar = foo < 100
print bar  # True

# 十进制浮点型

from decimal import Decimal

print Decimal('0.1')  # 0.1
# print  1.0 + Decimal('0.1')
