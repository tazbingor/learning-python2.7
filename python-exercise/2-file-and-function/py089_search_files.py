#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/4 下午7:40
# @Author  : Aries
# @Site    : 
# @File    : py089_search_files.py
# @Software: PyCharm
'''
9–18. 搜索文件. 提示输入一个字节值(0 - 255)和一个文件名. 显示该字符在文件中出现的次数.
'''
# import string


def search_files(file_name, bt_number):
    f = open(file_name, 'r')
    lines = f.readlines()
    value = chr(bt_number)
    # print lines
    # print value
    f.close()
    return sum([value.count(line) for line in ''.join(lines)])


# def count_words(s):
#     words = string.split(s)
#     return len(words)


if __name__ == '__main__':
    file_name = raw_input('请输入一个文件名:\n').strip()
    bt = int(raw_input('请输入一个字节值(0 - 255):\n').strip())
    if 0 < bt < 255 and isinstance(bt, int):
        print search_files(file_name, bt)
