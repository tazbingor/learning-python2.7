#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/9 上午8:53
# @Author  : Aries
# @Site    : 
# @File    : py111_print_str_recursion.py
# @Software: PyCharm
'''
11–15.递归。
从写练习6-5 的解，用递归向后打印一个字符串。用递归向前以及向后打印一个字符串。
'''


def forwardString(string, index=0):
    # result = ''
    if index < len(string):
        # result = string[0:index + 1]
        print string[0:index + 1]
        forwardString(string, index + 1)
        # return result


def backwardString(string, index=0):
    # result = ''
    if index > -len(string):
        # result = string[index - 1:]
        print string[index - 1:],
        backwardString(string, index - 1)
        # return result


def main():
    test_str = 'ABCDEFG'
    forwardString(test_str)
    print '-' * 50
    backwardString(test_str)


if __name__ == '__main__':
    main()
