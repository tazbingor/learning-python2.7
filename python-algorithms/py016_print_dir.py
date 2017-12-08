#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午12:24
# @Author  : Aries
# @Site    : 
# @File    : py016_print_dir.py.py
# @Software: PyCharm
'''
递归:打印指定目录下的所有文件(目录)
'''
import os


def print_dir(dirPath):
    for eachItem in os.listdir(dirPath):
        f = os.path.join(dirPath, eachItem)
        if os.path.isdir(f):
            print_dir(f)
        else:
            print f
