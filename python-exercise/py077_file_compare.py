#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/29 下午6:16
# @Author  : Aries
# @Site    : 
# @File    : py077_file_compare.py
# @Software: PyCharm
'''
9-6 文件对比,写一个比较两个文本文件的程序
如若不同,给出第一个不同处的行号和列号
'''


def fileCompare(filePath1, filePath2):
    row = 0
    col = 0
    with open(filePath1, 'r') as f1, open(filePath2, 'r') as f2:
        f1Line = f1.readlines()
        f2Line = f2.readlines()
        for i in range(min(len(f1Line), len(f2Line))):

            if f1Line[i] != f2Line[i]:

                # 确定行
                row = i + 1
                # 确定列,字符串两两相对比
                col = colCompare(f1Line[i], f2Line[i])
                break

    return [row, col]


def colCompare(str1, str2):
    if not isinstance(str1, str) and not isinstance(str2, str):
        return -1

    index = 0
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            index = i + 1
            break
    return index


# test
# a = 'java'
# b = 'jython'
# print lineIndexCompare(a, b) py075_file_info.py py076_file_access.py
result = fileCompare('py075_file_info.py', 'py076_file_access.py')
print '两文件第一处不相同的在第%s行,第%s列' % (str(result[0]), str(result[1]))
