#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/4 下午8:08
# @Author  : Aries
# @Site    : 
# @File    : py090_create_file.py
# @Software: PyCharm
'''
9–19. 创建文件.
创建前一个问题的辅助程序. 创建一个随机字节的二进制数据文件, 但某一特定字节会在文件中出现指定的次数. 该程序接受三个参数:
1) 一个字节值( 0 - 255 ),
2) 该字符在数据文件中出现的次数, 以及
3) 数据文件的总字节长度.
你的工作就是生成这个文件, 把给定的字节随机散布在文件里, 并且要求保证给定字符在文件中只出现指定的次数, 文件应精确地达到要求的长度.

'''
import random

# 搜索文件中文字出现的次数
def search_files(file_name, bt_number):
    f = open(file_name, 'r')
    lines = f.readlines()
    value = chr(bt_number)

    f.close()
    return sum([value.count(line) for line in ''.join(lines)])


# 创建文件
def create_file(bt_num, count, length_bt):
    user_input = raw_input('请输入文件名:\n')
    f = open(user_input, 'w')
    str_file = getBtList(bt_num, search_files(user_input, 112), length_bt - count)


def getBtList(value, n, count):
    ls = []
    for i in range(n):
        ran = random.randint(0, 255)
        if ran != value:
            ls.append(chr(ran))
        elif ran == value and value == 0:
            ran = random.randint(1, 255)
            ls.append(chr(ran))
        elif ran == value and value == 255:
            ran = random.randint(0, 254)
            ls.append(chr(ran))
        elif ran == value:
            ran = random.randint(0, value - 1)
            ls.append(chr(ran))
    for i in range(count):
        ls.insert(random.randint(0, n), chr(value))

    return ls


if __name__ == '__main__':
    pass
