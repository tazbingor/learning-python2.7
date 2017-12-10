#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/20 下午6:05
# @Author  : Aries
# @Site    : 
# @File    : py056_human_resources.py
# @Software: PyCharm
'''
人力资源。
创建一个简单的雇员姓名和编号的程序。让用户输入一组雇员姓名和编号。
你的程序可以提供按照姓名排序输出的功能，雇员姓名显示在前面，后面是对应的雇员编号。
附加题：添加一项功能，按照雇员编号的顺序输出数据。

'''

dict1 = {}
dict2 = {}
while True:
    name = raw_input('pls input a worker name: ')
    if name == '--':
        break
    number = int(raw_input('pls input a worker number: '))
    print '职员已录入完毕,输入\'--\'显示名单'
    dict1[name] = number
    dict2[number] = name

for key in sorted(dict1):
    print key, dict1[key]
print
print 'ID排列名单'
for key in sorted(dict2):
    print key, dict2[key]
