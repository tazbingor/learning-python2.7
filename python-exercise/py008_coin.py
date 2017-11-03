#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/3 下午1:40
# @Author  : Aries
# @Site    : 
# @File    : py008_coin.py
# @Software: PyCharm
'''
美刀问题
 1美刀能换100个一美分
	能换20个五美分
	能换10个十美分
	能换4个二十五美分

'''


def money(num):
    num *= 100
    a = num // 25
    b = (num - a * 25) // 10
    c = (num - a * 25 - b * 10) // 5
    d = (num - a * 25 - b * 10 - c * 5)
    return a + b + c + d


n = float(raw_input("input dollors:"))
print money(n)
