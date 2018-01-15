#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午8:04
# @Author  : Aries
# @Site    : 
# @File    : py164_match_redata.py
# @Software: PyCharm
'''
15-18.通过检查每个输出行中整型字段部分的第一个整型是否和该行开头的时间戳相匹配来验证redata.txt中的数据是否完好。
'''
from re import match
from time import mktime, strptime


def check_redata(path=''):
    with open(path) as f:
        for line in f:
            m = match('(.+)::.+::(\d+)', line)
            if m is not None:
                time1 = mktime(strptime(m.group(1)))
                time2 = float(m.group(2))
                if time1 == time2:
                    return line, '...well'


if __name__ == '__main__':
    print check_redata('redata.txt')
    # ('Wed Aug 28 19:25:30 2047::zlzdp@qmybv.org::2450604330-5-5\n', '...well')
