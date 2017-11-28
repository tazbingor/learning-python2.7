#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/28 下午9:04
# @Author  : Aries
# @Site    : 
# @File    : py073_file_screening.py
# @Software: PyCharm
'''
9-1.文件过滤
显示一个文件的所有行,忽略以#号开头的行.这个字符被用作Python,Perl,Tcl,等大多脚本文件的注释符号
附加题:处理不是第一个字符开头的注释
'''


def filePrint(filePath):
    file1 = open(filePath, 'r')
    for line in file1:
        # if line[0] != '#':
        #     print line
        if line.startswith('#'):
            continue
        elif '#' in line:
            print line[:line.find('#')]
        else:
            print line

    file1.close()


filePrint('py072_bit_manipulation.py')
