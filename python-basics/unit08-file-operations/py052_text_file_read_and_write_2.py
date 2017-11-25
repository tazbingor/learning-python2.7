#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/25 下午4:03
# @Author  : Aries
# @Site    : 
# @File    : py052_text_file_read_and_write_2.py
# @Software: PyCharm
'''
python文件读写方式2
文件迭代器
'''
file1 = open('test1.txt', 'w')
for line in open('poem.txt'):
    file1.write(line)

file1.close()
