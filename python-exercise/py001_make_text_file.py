#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/10/31 下午5:29
# @Author  : Aries
# @Site    : 
# @File    : py001_make_text_file.py
# @Software: PyCharm
# 文件写入

'''
提醒用户创建一个文件名,同时输入每一行,然后将文本写入文本文件
'''
import os

ls = os.linesep

while True:
    fname = raw_input('输入文件名: ')
    if os.path.exists(fname):
        print "ERROR: '%s' already exists" % fname
    else:
        break

all = []
print "\n 输入文件内容: ('.' by itself to quit).\n"

while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

fobj = open(fname, 'w')  # 打开文件
fobj.write('\n'.join(all))  # 写入
fobj.close()  # 关闭文件流
print 'DONE!'
