#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/27 下午5:44
# @Author  : Aries
# @Site    : 
# @File    : py127_authorization.py
# @Software: PyCharm
'''
13-15 授权
    示例13.8的执行结果表明我们的类的CapOpen能成功完成数据的写入操作.在我们的最后的评论,
    提到可以使用CapOpen()或open()来读取文件中的文本,为啥呢?使用起来有什么差异吗?

'''


class CapOpen(object):
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return 'self.file'

    def write(self, line):
        self.file.write(line.upper())

    def __getattr__(self, item):
        return getattr(self.file, item)


'''
并没有多大的差异,类CapOpen读取文件也是调用内建函数open(),只是类CapOpen中有更多操作文件的函数,使用起来更方便
'''
