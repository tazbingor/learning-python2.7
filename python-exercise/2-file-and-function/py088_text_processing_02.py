#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/4 下午7:00
# @Author  : Aries
# @Site    : 
# @File    : py088_text_processing_02.py
# @Software: PyCharm
'''
9–17. 文本处理.
创建一个原始的文本文件编辑器. 你的程序应该是菜单驱动的, 有如下这些选项:
1) 创建文件(提示输入文件名和任意行的文本输入),
2) 显示文件(把文件的内容显示到屏幕),
3) 编辑文件(提示输入要修改的行, 然后让用户进行修改),
4) 保存文件, 以及
5) 退出.
'''
import os


# 1.创建文件
def create_text():
    user_input = raw_input('请输入文件名(如\"test.txt\"或\"test\"):\n')
    if '.txt' not in user_input:
        user_input += '.txt'

    print('请输入内容,按command+d退出并保存文档:\n')
    f = open(user_input, 'w')
    while True:
        try:
            f.write(raw_input() + "\n")
        except (EOFError, KeyboardInterrupt, IndexError):
            f.close()
            break


# 2.展示文件
def show_text(user_input):
    path = os.path.join(os.getcwd(), user_input)
    f = open(path, 'r')
    for eachLine in f:
        print eachLine
    f.close()


# 3.编辑文件
def edit_text(user_input, col, editStr):
    path = os.path.join(os.getcwd(), user_input)
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    lines[col] = editStr
    return lines


# 4. 保存文件
def save_text(user_input, lines):
    f = open(user_input, 'w')
    for line in lines:
        f.write(line)
    f.close()


if __name__ == '__main__':
    filename = ''
    ls = []
    while True:
        print '\n'
        print '1. create a file'
        print '2. show a file'
        print '3. edit a file'
        print '4. save a file'
        print '5. quit'

        ch = raw_input('input a choice:')
        if ch not in '1234':
            break
        elif ch == '1':
            filename = raw_input('input a file name:\n')
            create_text(filename)
        elif ch == '2':
            filename = raw_input('input a file name:\n')
            show_text(filename)
        elif ch == '3':
            if filename == '':
                filename = raw_input('file name: ')
            index = int(raw_input('input a index of line:'))
            content = raw_input('pls input a line:')
            ls = edit_text(filename, index, content)
        elif ch == '4':
            save_text(filename, ls)
