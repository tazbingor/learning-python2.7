#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/3 下午6:23
# @Author  : Aries
# @Site    : 
# @File    : py137_open_evo.py
# @Software: PyCharm
'''
10-6.改进open() 为內建的open()函数创建一个封装.使得成功打开文件后,返回文件句柄:
    若打开失败则返回给调用者None,而不是生成一个异常
'''


def evolution_open(path, opt='r'):
    try:
        f = open(path, opt)
    except IOError:
        return None
    return f


if __name__ == '__main__':
    f = evolution_open('test.txt')
    print f.readlines()

    f1 = evolution_open('1.txt')
    print f1  # None
