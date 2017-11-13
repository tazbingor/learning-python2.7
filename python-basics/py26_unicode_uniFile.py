#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/13 下午3:11
# @Author  : Aries
# @Site    : 
# @File    : py26_unicode_uniFile.py
# @Software: PyCharm
'''
python unicode
'''
CODEC = 'utf-8'
FILE = 'unicode.txt'

# 写入文本
hello_out = u'python'
bytes_out = hello_out.encode(CODEC)  # UTF8 格式化
f = open(FILE, 'w')
f.write(bytes_out)
f.close()

# 读取
f = open(FILE, 'r')
bytes_in = f.read()
f.close()
hello_in = bytes_in.encode(CODEC)
print hello_in,
