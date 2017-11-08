#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/8 下午5:39
# @Author  : Aries
# @Site    : 
# @File    : py029_test_codes.py
# @Software: PyCharm
'''
测试代码
下 的代码x=4时会发 什么情况?
while True :
    for x in range(6):
        y = 2*x + 1
        pint y
        if y>9 :
            break

答:当X=4时,输出为9(而且会输出无数次),但条件下的break职能跳出本层循环,并不会跳出外层循环,因为外层循环是无限循环
所以,程序到最后会抛出内存溢出的异常
'''

while True:
    for x in range(6):
        y = 2 * x + 1
        print y
        if y > 9:
            break
