#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/20 下午9:40
# @Author  : Aries
# @Site    : 
# @File    : py060_calculator.py
# @Software: PyCharm
'''
集合计算器

编写一个程序允许用户选择两个集合:A 和 B, 及运算操作符。例如，in, not in, &, |, ^, <, <=, >, >=, ==, !=, 等.
(你自己定义集合的输入语法，它们并不一定要像 Java 示例中那样用方括 号括住。)
解析输入的字符串，按照用户选择的运算进行操作。你写的程序代码应该比 Java 版本的 该程序更简洁。
'''


def setCalculator(set1, set2, opt):
    return eval(str(set1) + str(opt) + str(set2))


set1 = set('JavaScript')
set2 = set('JavaSE')

opts = {' in ', ' not in ', '&', '|', '^', '<', '<=', '>', '>=', '==', '!='}
for opt in opts:
    print '([%s]) %s ([%s]) is: %s' % (set1, opt, set2, setCalculator(set1, set1, opt))
