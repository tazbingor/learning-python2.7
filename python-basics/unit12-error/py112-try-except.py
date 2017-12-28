#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/28 下午9:38
# @Author  : Aries
# @Site    : 
# @File    : py112-try-except.py
# @Software: PyCharm
'''
try-except 语句
'''


def open_file(path, opt='rb'):
    try:
        f = open(path, opt)
    except IOError, e:
        print '文件输入输出操作异常:', e


if __name__ == '__main__':
    f = open_file('something')  # 文件输入输出操作异常: [Errno 2] No such file or directory: 'something'
    pass
'''
注意: try语句中的某一句一旦出现异常,那么try中的剩余代码将被忽略,
转而执行 except 的处理异常操作
'''
