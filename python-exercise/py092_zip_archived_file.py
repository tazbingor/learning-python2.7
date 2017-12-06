#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午6:31
# @Author  : Aries
# @Site    : 
# @File    : py092_zip_archived_file.py
# @Software: PyCharm
'''
9–21. ZIP 归档文件.
创建一个程序, 可以往 ZIP 归档文件加入文件, 或从中提取文件,有可能的话, 加入创建ZIP 归档文件的功能.

'''

import zipfile


def create_zipfile(zipname, filename1, filename2):
    z = zipfile.ZipFile(zipname, 'w')
    z.write(filename1)
    z.write(filename2)
    z.close()


def add_zipfile(zipname, filename):
    z = zipfile.ZipFile(zipname, 'a')
    z.write(filename)
    z.close()


def extract_zipfile(zipname, filename):
    z = zipfile.ZipFile(zipname, 'r')
    z.extract(filename)
    z.close()


if __name__ == '__main__':
    create_zipfile(r'test.zip', r'test.txt', r'test1.txt')
    add_zipfile(r'test.zip', r'test2.txt')
    extract_zipfile(r'test.zip', r'test.txt')
