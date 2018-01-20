#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午1:02
# @Author  : Aries
# @Site    : 
# @File    : py083_recursion_binary_search.py
# @Software: PyCharm
'''
递归:二分查找
    当我们对一个列表执行二分搜索时,我们首先选择中间项。如果搜索项比中间项
小,我们可以在原来列表的左半部分执行二分搜索,同样地,如果搜索项更大,我们可以在右半 部分执行二分搜索。
'''

numlist = [1, 3, 5, 7, 9]


def binarySearchRecu(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid_point = len(alist) // 2
        if alist[mid_point] == item:
            return True

        else:
            if item > alist[mid_point]:
                return binarySearchRecu(alist[mid_point + 1:], item)
            else:
                return binarySearchRecu(alist[:mid_point], item)


if __name__ == '__main__':
    print binarySearchRecu(numlist, 2)  # False
    print binarySearchRecu(numlist, 7)  # True


# mid_point = len(numlist) / 2
# print mid_point
