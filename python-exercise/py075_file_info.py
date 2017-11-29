#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/29 下午5:17
# @Author  : Aries
# @Site    : 
# @File    : py075_file_info.py
# @Software: PyCharm
'''
9-3 文件信息,提示输入一个文件名,然后显示这个文本文件的总行数
'''


def fileInfo(filePath):
    file1 = open(filePath, 'r')
    lineCount = file1.readlines()
    file1.close()
    return len(lineCount)


print fileInfo('py074_file_reference.py')
