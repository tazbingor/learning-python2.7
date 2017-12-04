#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/4 下午3:45
# @Author  : Aries
# @Site    : 
# @File    : py084_Command_line_parameter.py
# @Software: PyCharm
'''
9–13. 命令行参数
a) 什么是命令行参数, 它们有什么用?
命令行参数是调用某个程序时除程序名以外的其他参数。命令行参数使程序员可以在启动一个程序时对程序行为作出选择。
b) 写一个程序, 打印出所有的命令行参数.
'''
import sys

print str(sys.argv)  # 输出路径名
