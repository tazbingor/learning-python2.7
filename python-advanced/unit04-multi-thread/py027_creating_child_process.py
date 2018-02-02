#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/2/2 下午11:17
# @Author  : Aries
# @Site    : 
# @File    : py027_creating_child_process.py
# @Software: PyCharm
'''
创建子进程

此代码在windows上无法运行,因为没有fork调用
'''
import os

print 'process(%s) start...' % os.getgid()

pid = os.fork()

if pid == 0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)
    # # process(20) start...
    # I (5068) just created a child process (5069).
    # I am child process (5069) and my parent is 5068.
