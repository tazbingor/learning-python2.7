#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/3 下午2:22
# @Author  : Aries
# @Site    : 
# @File    : py009_calculator.py
# @Software: PyCharm
'''
python计算器

比如用户输入 8,"*",8时,结果为64,
不得使用eval()内建函数
'''


def myCalculator(number1, str_opt, number2):
    result = 0
    if str_opt == '+':
        result = number1 + number2
    elif str_opt == '-':
        result = number1 - number2
    elif str_opt == '*':
        result = number1 * number2
    elif str_opt == '/':
        result = number1 / number2
    elif str_opt == '%':
        result = number1 % number2
    elif str_opt == '**':
        result = number1 ** number2
    return result


ss = raw_input("input your expression:")
if len(ss) == 3:
    print myCalculator(float(ss[0]), ss[1], float(ss[2]))
else:
    print myCalculator(float(ss[0]), ss[1:3], float(ss[3]))
