#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/2 下午2:43
# @Author  : Aries
# @Site    : 
# @File    : py003_display_num_type_dir.py
# @Software: PyCharm

# 函数displayNumType()的翻版,新建函数displayDir(),查询obj中所有的属性

class testA:
    def run(self): pass

    def eat(self): pass

    def sleep(self): pass


def displayDir(obj):
    return dir(obj)


print displayDir(testA)  # ['__doc__', '__module__', 'eat', 'run', 'sleep']
