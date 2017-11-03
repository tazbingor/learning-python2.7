#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/3 下午3:56
# @Author  : Aries
# @Site    : 
# @File    : py012_Fahrenheit.py
# @Software: PyCharm
# 华氏度转换

# print 5.0 / 9

def getCentigrade(fahrenheit):
    return (fahrenheit - 32) * (5.0 / 9)


user_input = int(raw_input("请输入你想转换的温度\n"))
print str(getCentigrade(user_input)) + "°C"
