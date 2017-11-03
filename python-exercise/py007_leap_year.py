#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/3 下午1:20
# @Author  : Aries
# @Site    : 
# @File    : py007_leap_year.py
# @Software: PyCharm
# 判断公元1年到公元3000年中那些是闰年

leap_year = []
for year in range(1, 3001):
    if year % 4 == 0 and (year % 100 != 0 or year % 100 == 0):
        leap_year.append(year)
        print "%s是闰年." % repr(year)
print leap_year
print "其中有%s个闰年" % repr(len(leap_year))
