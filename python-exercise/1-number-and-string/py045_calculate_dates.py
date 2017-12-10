#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/17 下午7:30
# @Author  : Aries
# @Site    : 
# @File    : py045_calculate_dates.py
# @Software: PyCharm
'''
计算日期

转换。

(a)给出两个可识别格式的日期，比如MM/DD/YY或者DD/MM/YY格式。计算出两个日期之间的天数。
(b)给出一个人的生日，计算此人从出生到现在的天数，包括所有的闰月。
(c)还是上面的例子，计算出此人下次过生日还有多少天。

'''
import datetime


# date = '10/01/2017'
# print ''.join(date)

def convertDate(allDate):
    aYear = int(allDate.split("/")[-1])
    aMonth = int(allDate.split("/")[0])
    aDay = int(allDate.split("/")[1])
    return (aYear, aMonth, aDay)


Dt = raw_input("Enter a date ...\n")
D1 = datetime.date(convertDate(Dt)[0], convertDate(Dt)[1], convertDate(Dt)[2])
Dt = raw_input("Enter another date ...\n")
D2 = datetime.date(convertDate(Dt)[0], convertDate(Dt)[1], convertDate(Dt)[2])
print (D2 - D1).days
