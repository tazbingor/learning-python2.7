#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午5:17
# @Author  : Aries
# @Site    : 
# @File    : py102_variable_parameter.py
# @Software: PyCharm
'''
11-6.
变长参数。写一个称为printf()的函数。有一个值参数，格式字符串。
剩下的就是根据格式化字符串的值，要显示在标准输出上的可变参数，格式化字符串中的值允许特别的字符串格式操作指示符，
如%d，%f，etc。提示：解是很琐碎的--无需实现字符串操作符功能性，但你需要显示用字符串格式化操作（%）。
'''


def printf(log, *args):
    print log % args


if __name__ == '__main__':
    printf('%s', 'Python')  # Python
