#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/29 上午11:18
# @Author  : Aries
# @Site    : 
# @File    : py006_while.py
# @Software: PyCharm
# while

# 输出1-10
# i = 0
# while i < 10:
#     i += 1
#     print i

# 输出 1 到10, 5不输出
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    else:
        print i
