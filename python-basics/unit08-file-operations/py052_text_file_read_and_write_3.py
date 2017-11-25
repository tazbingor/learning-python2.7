#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/25 下午4:11
# @Author  : Aries
# @Site    : 
# @File    : py052_text_file_read_and_write_3.py
# @Software: PyCharm
'''
python文件读写方式3,上下文管理器
'''
file1 = open('test2.txt','w')
with open('poem.txt','r') as file2:
    for line in file2:
        file1.write(line[:])
file1.close()