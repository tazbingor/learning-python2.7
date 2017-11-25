#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/25 下午3:51
# @Author  : Aries
# @Site    : 
# @File    : py051_text_file_read_and_write_1.py
# @Software: PyCharm
'''
python 文本文件读写方式1
读一行写一行
'''

# 打开文件流
file1 = open('poem.txt', 'r')
file2 = open('new poem.txt', 'w')

while True:
    # 读写文件
    line = file1.readline()
    file2.write(line[:])
    if not line:
        break

# 关闭文件流
file1.close()
file2.close()
