#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/11 下午8:02
# @Author  : Aries
# @Site    : 
# @File    : py009_sub.py
# @Software: PyCharm
'''
re 高级用法

sub 将匹配到的数据进行替换
'''
import re


def str_sub(string, substr=''):
    return re.sub('\\d*[.]\\d*', substr, string)


if __name__ == '__main__':
    # 查找字符串中的数字,并修改
    print str_sub('推荐使用python2.7版本', '3.6')  # 推荐使用python3.6版本
