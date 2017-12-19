#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/19 下午4:15
# @Author  : Aries
# @Site    : 
# @File    : py100_class_changeable_type.py
# @Software: PyCharm
'''
可变类型

'''


# 字典排序
class SortedKeyDict(dict):
    def keys(self):
        return sorted(super(SortedKeyDict, self).keys())


# 映射类型子类化
class SortedNewKeyDict(dict):
    def keys(self):
        return sorted(self.keys())  # 这种方式属于递归


if __name__ == '__main__':
    temp_dict = SortedKeyDict((('C', 3), ('B', 2), ('A', 1)))
    print [key for key in temp_dict]  # ['A', 'C', 'B']
    print temp_dict.keys()  # ['A', 'B', 'C']

    print '-' * 50
    # temp_dict1 = SortedNewKeyDict((('C', 3), ('B', 2), ('A', 1)))
    # print temp_dict1.keys()  # RuntimeError: maximum recursion depth exceeded
