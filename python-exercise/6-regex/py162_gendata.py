#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午7:16
# @Author  : Aries
# @Site    : 
# @File    : py162_gendata.py
# @Software: PyCharm
'''
15-16.修改gendata.py的代码，使数据直接写入文件redata.txt中，而不是输出到屏幕上。

'''
from random import randrange, choice
from string import lowercase
# from sys import maxint
from time import ctime
from os import linesep

doms = ('com', 'edu', 'net', 'org', 'gov')


def gendata():
    string = ''
    f = open('redata.txt', 'w')
    for i in range(randrange(5, 10)):
        data_int = randrange(2 ** 32)  # pick date
        data_str = ctime(data_int)

        shorter = randrange(4, 7)
        em = time_change_str(shorter)

        longer = randrange(shorter, 12)
        dn = time_change_str(longer)

        string = '%s::%s@%s.%s::%d-%d-%d' \
                 % (data_str, em, dn, choice(doms), data_int, shorter, longer)
        string += linesep
    f.write(string)
    f.close()


def time_change_str(shorter):
    string = ''
    for i in range(shorter):
        string += choice(lowercase)
    return string


if __name__ == '__main__':
    gendata()
