#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午6:37
# @Author  : Aries
# @Site    : 
# @File    : py_093_lszip.py.py
# @Software: PyCharm
'''
9–22. ZIP 归档文件.
unzip -l 命令显示出的 ZIP 归档文件很无趣. 创建一个 Python脚本 lszip.py ,
使它可以显示额外信息: 压缩文件大小, 每个文件的压缩比率(通过比较压缩前后文件大小), 以及完成的 time.ctime() 时间戳,
而不是只有日期和 HH:MM .
提示: 归档文件的 date_time 属性并不完整, 无法提供给 time.mktime() 使用....这由你自己决定.
'''

import zipfile
import os
import time

filename = raw_input('zip file name:')
print 'zip file size: %d bytes' % (os.stat(filename).st_size)
z = zipfile.ZipFile(filename, 'r')
print 'filename\tdatetime\tsize\tcompress size\trate'
for info in z.infolist():
    t = time.ctime(time.mktime(tuple(list(info.date_time) + [0, 0, 0])))
    print '%s\t%s\t%d\t%d\t%.2f%%' % (
        info.filename, t, info.file_size, info.compress_size, float(info.compress_size) / info.file_size * 100)
z.close()
