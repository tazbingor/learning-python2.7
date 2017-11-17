#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/2 上午10:58
# @Author  : Aries
# @Site    : 
# @File    : py012_builtin_functions_cmp.py
# @Software: PyCharm

'''
python 内建对象 isinstance
'''


# 函数displayNumType() 接收一个参数,并使用type确认他的类型

def displayNumType(obj):
    # if obj == None or bool(obj):
    #     print("不要输入空字符串!")
    #     return 0

    if isinstance(obj, (int, long, float, complex)):
        print type(obj).__name__
    else:
        print "此对象不属于number"


displayNumType(100)
displayNumType("100")

displayNumType(100L)
displayNumType(100J)
displayNumType(100.0)
