#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/5 下午4:11
# @Author  : Aries
# @Site    : 
# @File    : py018_comparison_value.py
# @Software: PyCharm
# 比较值

print False and None  # False
print 0 and None  # 0
print 0 and None or () and []  # ()
print True and None or () and []  # ()
print 0 or None and () or []  # []
print True or None and () or []  # True
print 1 or None and 'a' or 'b'  # 1
