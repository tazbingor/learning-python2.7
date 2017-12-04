#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/3 下午10:42
# @Author  : Aries
# @Site    : 
# @File    : py083_username_pwd.py
# @Software: PyCharm
'''
9-12 用户名和密码。
回顾练习7-5，修改代码使之可以支持“上次登录时间”。请参阅time模块中的文档了解如何记录用户上次登录的时间。
另外提供一个系统管理员，他可以导出所有用户的用户名，密码（如需要可以加密），以及上次登录时间。
a）数据应保存在磁盘中，使用冒号：分隔，一次写入一行，例如“Joe：boohoo：953176591.145，文件中数据的行数应该等于你系统上的用户数。
b）进一步改进你的程序，不再一次写入一行，而使用pickle模块保存整个数据对象。请参阅pickle模块的文档了解如何序列化/扁平化对象，以及如何读写保存的对象。
一般来说，这个解决方案的代码行数要比a）少；
c）使用shelve模块替换pickle模块，由于可以省去一些维护代码，这个解决方案的代码比b）的更少。
'''
import time

