#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 上午11:39
# @Author  : Aries
# @Site    : 
# @File    : py047_file_iter.py
# @Software: PyCharm
'''
文件迭代
'''

myFile = open('py046_dict_iter.py')
for item in myFile:
    print item

myFile.close()
