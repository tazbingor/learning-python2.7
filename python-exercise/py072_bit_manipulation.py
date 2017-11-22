#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 下午6:21
# @Author  : Aries
# @Site    : 
# @File    : py072_bit_manipulation.py
# @Software: PyCharm
'''
8-12 :（整形）位操作。
编写一个程序，用户给出起始和结束数字后给出一个下面的表格，分别显示两个数字间的十进制、二进制、八进制和十六进制。
如果字符是可打印的ASCII字符，也要打印出来，如果没有一个是可打印的就省略ASCII那一栏的表头。

'''


def outPut(start, end):
    if start >= 33 or end <= 126:
        print '%-10s%-10s%-10s%-10s%-10s' % ('DEC', 'BIN', 'OCT', 'HEX', 'ASCII')
        print '---------------------------------------------'
    else:
        print '%-10s%-10s%-10s%-10s' % ('DEC', 'BIN', 'OCT', 'HEX')
        print '---------------------------'
    for i in range(start, end + 1):
        if start >= 33 or end <= 126:
            print '%-10d%-10s%-10s%-10s' % (i, bin(i), oct(i), hex(i)),
            if i >= 33 and i <= 126:
                print '%-10s' % chr(i)
            else:
                print '%-10s' % ' '
        else:
            print '%-10d%-10s%-10s%-10s' % (i, bin(i)[2:], oct(i)[1:], hex(i)[2:],)


start = input('Please input start number:')
end = input('Please input end number:')
outPut(start, end)
