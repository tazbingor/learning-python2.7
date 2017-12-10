#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午6:29
# @Author  : Aries
# @Site    : 
# @File    : py106_functional_filter_dirpath.py
# @Software: PyCharm
'''
11-10.
用filter()进行函数式编程。在unix文件系统中，在每个文件夹或者目录中都有两个特别的文件："."表示现在的目录，".."表示父目录。
给出上面的知识，看一下os.listdir()函数的文档并描述这段代码做了什么：
files = filter(lambda x: x and x[0] != '.', os.listdir(folder))
'''
import os

# 假设folder是path
FOLDER = 'rising-python-classics/python-algorithms'


def main():
    files = filter(lambda x: x and x[0] != '.', os.listdir(FOLDER))
    print files  # 返回的是当前文件夹(路径)下的所有文件的列表


if __name__ == '__main__':
    main()
