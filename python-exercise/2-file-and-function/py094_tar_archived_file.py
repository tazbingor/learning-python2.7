#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午6:40
# @Author  : Aries
# @Site    : 
# @File    : py094_tar_archived_file.py
# @Software: PyCharm
'''
9–23. TAR 归档文件.
为 TAR 归档文件建立类似上个问题的程序.
这两种文件的不同之处在于 ZIP 文件通常是压缩的, 而 TAR 文件不是, 只是在 gzip 和 bzip2 的支持下才能完成压缩工作.
加入任意一种压缩格式支持.附加题: 同时支持 gzip 和 bzip2 .

'''
import tarfile


def create_tarfile(tarname, filename1, filename2):
    t = tarfile.open(tarname, 'w:gz')  # w:bz2
    t.add(filename1)
    t.add(filename2)
    t.close()


def extract_tarfile(tarname):
    t = tarfile.open(tarname, 'r')
    t.extractall(r'D:\test')
    t.close()


if __name__ == '__main__':
    create_tarfile(r'test.tar.gz', r'test.txt', r'test1.txt')
    extract_tarfile(r'test.tar.gz')
