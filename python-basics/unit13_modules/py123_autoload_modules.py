#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/5 下午11:43
# @Author  : Aries
# @Site    : 
# @File    : py123_autoload_modules.py
# @Software: PyCharm
'''
自动载入的模块
'''
import sys

if __name__ == '__main__':
    print sys.modules.keys()
# ['copy_reg', 'sre_compile', '_sre', 'site', '__builtin__', 'sysconfig',
# '__main__', 'abc', 'posixpath', '_weakrefset', 'errno', 'sre_constants',
# 're', '_abcoll', 'types', '_warnings', 'genericpath', 'stat', 'zipimport', '
# _sysconfigdata', 'mpl_toolkits', 'warnings', 'UserDict', 'sys', '_osx_support',
#  'os.path', '_locale', 'signal', 'traceback', 'linecache', 'posix', 'exceptions',
# 'sre_parse', 'os', '_weakref']

'''
不同的系统,不同运行环境下,一些模块会被解释器自动导入
'''