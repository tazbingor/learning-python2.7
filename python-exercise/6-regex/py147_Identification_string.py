#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/12 下午5:16
# @Author  : Aries
# @Site    : 
# @File    : py147_Identification_string.py
# @Software: PyCharm
'''
15-1 识别下列字符串:'bat','bit','but','hat','hit','hut'
'''
import re


def identif_string(string=''):
    try:
        return re.match(r'[bh][aiu]t,?', string).group()
    except AttributeError:
        return None


if __name__ == '__main__':
    # 测试
    print identif_string('bat')  # bat
    print identif_string('bit')  # bit
    print identif_string('but')  # but
    print identif_string('hat')  # hat
    print identif_string('hit')  # hit
    print identif_string('hut')  # hut
    print identif_string('git')  # None
