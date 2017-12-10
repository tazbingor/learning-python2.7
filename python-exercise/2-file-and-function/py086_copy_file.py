#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/4 下午6:30
# @Author  : Aries
# @Site    : 
# @File    : py086_copy_file.py
# @Software: PyCharm
'''
9–15. 复制文件. 提示输入两个文件名(或者使用命令行参数). 把第一个文件的内容复制到第二个文件中去.

'''


def copy_file(user_input_1, user_input_2):
    file1 = open(user_input_1, 'r')
    file2 = open(user_input_2, 'w')
    for eachLine in file1:
        file2.write(eachLine)
    file1.close()
    file2.close()


if __name__ == '__main__':
    user_input_1 = raw_input('请输入原文件路径:\n')
    user_input_2 = raw_input('请输入(或创建)目标文件路径:\n')
    copy_file(user_input_1, user_input_2)
