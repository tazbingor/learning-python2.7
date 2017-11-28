#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/28 下午9:51
# @Author  : Aries
# @Site    : 
# @File    : py074_file_reference.py
# @Software: PyCharm
'''
9-2 文件访问,提示输入数字N和文件F,然后显示文件F的钱N行

'''


def fileReference(num, filePath):
    if not isinstance(num, int) and not isinstance(filePath, str):
        return '请输入正确的参数类型'
    file1 = open(filePath, 'r')

    for count in range(num):
        print file1.readline()

    file1.close()


fileReference(7, 'py073_file_screening.py')
