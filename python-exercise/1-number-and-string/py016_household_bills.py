#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/5 上午11:58
# @Author  : Aries
# @Site    : 
# @File    : py016_household_bills.py
# @Software: PyCharm
# 每月家庭开支单

user_paid = float(raw_input("请输入每天的支出:\n"))
user_balance = float(raw_input("请输入每月初始资金:\n"))

day = 0
# temp = 0
while True:
    if day < 1:
        print "天数\t\t\t支出\t\t\t余额"
        print '-' * 30
    day += 1
    user_balance -= user_paid
    if user_balance > 0:
        print "%s\t\t\t%s元\t\t%s元" % (str(day), str(user_paid), str(user_balance))
    else:
        print "%s\t\t\t%s元\t\t%s元" % (str(day), str(user_paid - abs(user_balance)), str(0.0))
        break
