#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/7 下午4:07
# @Author  : Aries
# @Site    : 
# @File    : py066_grab_web.py
# @Software: PyCharm
'''
默认函数对象参数示例
抓取WEB页面
'''
from urllib import urlretrieve


def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
    else:
        return eachLine


def firstLast(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print  firstNonBlank()
    lines.reverse()
    print  firstNonBlank()


def download(url='http://www', process=firstLast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:
        process(retval)


if __name__ == '__main__':
    download()
