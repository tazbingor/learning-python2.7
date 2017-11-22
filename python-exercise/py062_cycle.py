#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 下午2:08
# @Author  : Aries
# @Site    : 
# @File    : py062_cycle.py
# @Software: PyCharm
'''
循环. 编写一个程序,让用户输入3个数字:(f)rom,(t)o和(i)ncrement. 以i为步长,从
   f计数到t,包括f和t. 例如,如果输入的是f==2,t==26,i==4,程序将输出2,6,10,14,18,
   22,26.
'''

print '设置循环范围'
f = int(raw_input('输入从哪个数开始\n'))
t = int(raw_input('输入从哪个数为止\n'))
i = int(raw_input('设置步长\n'))
print '-' * 50
for item in range(f, t, i):
    print item
