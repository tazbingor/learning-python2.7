#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/26 下午8:44
# @Author  : Aries
# @Site    : 
# @File    : py055_os.py
# @Software: PyCharm
'''
os 和os.path
创建一个文本文件写入少量数据,然后重命名,输出文件内容,同时还进行了一些辅助性的操作
比如遍历目录树和文件路径名的处理
'''

import os

for tmpdir in ('/tmp', r'/temp'):
    if os.path.isdir(tmpdir):
        break
        #
    else:
        print 'no temp directory available'
        tmpdir = ''

    if tmpdir:
        os.chdir(tmpdir)
        cwd = os.getcwd()
        print '*** current temporary directory'
        print cwd

        print '*** creating wxample directory...'

        os.mkdir('example')
        os.chdir('example')
        cwd = os.getcwd()
        print '*** new working directory: '
        print cwd
        print  '*** original directory listing: '
        print os.listdir(cwd)
