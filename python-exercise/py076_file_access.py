#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/29 下午5:26
# @Author  : Aries
# @Site    : 
# @File    : py076_file_access.py
# @Software: PyCharm
'''
9-4 文件访问
写一个逐页显示文本文件的程序.提示输入一个文件名,25行为一页,逐页显示,并在每页末尾提示用户"按任意键继续"
'''


def fileReader():
    filePath = raw_input('请输入一个文件名或者文件地址:\n')
    file1 = open(filePath, 'r')
    line = 1
    for eachLine in file1.readlines():
        if line % 26 == 0:
            raw_input('按任意键继续:')
        print line, '. ', eachLine
        line += 1
    file1.close()


if __name__ == '__main__':
    fileReader()
