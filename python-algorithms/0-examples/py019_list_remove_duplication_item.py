#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/15 上午11:29
# @Author  : Aries
# @Site    : 
# @File    : py019_list_remove_duplication_item.py
# @Software: PyCharm
'''
写一个函数，输入 lst = [1, 1, 3, 4, 4, 1]，返回值为[1,3,4,1]。

需求是：如果后一个数字与前一个数字相同，则只保留一个数。
'''


def format_list(alist):
    temp = []
    for index, value in enumerate(alist):
        if index == 0 or alist[index - 1] != value:
            temp.append(value)
    return temp


def main():
    lst = [1, 1, 3, 4, 4, 1]

    # for i, v in enumerate(lst):
    #     print i, ':', v

    print format_list(lst)


if __name__ == '__main__':
    main()

