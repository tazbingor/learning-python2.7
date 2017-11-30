#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/30 下午6:52
# @Author  : Aries
# @Site    : 
# @File    : py080_docstring.py
# @Software: PyCharm
'''
9-9 文档字符串
进入python标准库所在的目录.检查每一个.py文件是否有_doc_字符串,如果有,对其格式进行适当的整理归类.
你的程序执行完毕后,应该会生成一个漂亮的清单.里面列出哪些模块有文档字符串,以及文档字符串的内容,清单最后附上哪些没有文档字符串模块的名字
附加题:提取标准库中各个模块内的全部class和函数的文档
'''
import os
import sys


def get_doc_library(pyPath):
    f = open(r'chcekdoclists.txt', 'w')
    f.write('__doc__ in there files:nnn')
    temp = []
    for filename in os.walk(pyPath):
        for files in filename:
            if '__doc__' in files:
                f.write(files, ' : ', files.__doc__, 'nnn')
            else:
                temp.append(files)

    f.write('__doc__ not in there files:nnn')
    for i in temp:
        f.write(i + 'nnn')

    f.close()

def get_mod_class(pyPath):
    pass

def get_mod_functions(pyPath):
    pass

