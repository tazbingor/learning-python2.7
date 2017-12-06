#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午6:14
# @Author  : Aries
# @Site    : 
# @File    : py091_compressed_files.py
# @Software: PyCharm
'''
9–20. 压缩文件.
写一小段代码, 压缩/解压缩 gzip 或 bzip 格式的文件.
可以使用命令行下的 gzip 或 bzip2 以及 GUI 程序 PowerArchiver , StuffIt , 或 WinZip 来确认你的 Python支持这两个库.

'''
import gzip


# 压缩
def compressed_file(filepath):
    file_in = open(filepath, 'rb')
    file_out = open(filepath + '.gz', 'wb')
    file_out.writelines(file_in)
    file_out.close()
    file_in.close()


def uncompress_file(zippath, outpath):
    file_in = gzip.open(zippath, 'rb')
    file_out = open(outpath, 'wb')
    content = file_in.read()
    file_out.write(content)
    file_in.close()
    file_out.close()


if __name__ == '__main__':
    # pass
    # compressed_file('test.txt')
    uncompress_file('test.txt.gz', 'test(副本).txt')
