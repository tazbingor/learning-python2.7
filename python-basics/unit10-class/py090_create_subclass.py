#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/11 下午8:42
# @Author  : Aries
# @Site    : 
# @File    : py090_create_subclass.py
# @Software: PyCharm
'''
创建子类
'''


class MyClass(object):
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age


class MyNewClass(object):
    def __init__(self, name, age, ID, native_place):
        MyClass.__init__(self, name, age)
        self.ID = ID
        self.native_place = native_place

    def get_place(self, np):
        self.native_place = np


if __name__ == '__main__':
    pass
