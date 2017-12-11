#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/11 下午8:29
# @Author  : Aries
# @Site    : 
# @File    : py089_create_class.py
# @Software: PyCharm
'''
定义类

'''


class MyClass(object):
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def personal_information(self, ID):
        self.ID = ID


if __name__ == '__main__':
    # 实例化类
    new_class = MyClass('xb', 24)
    print new_class  # <__main__.MyClass object at 0x10a020390>
    print type(new_class)  # <class '__main__.MyClass'>
    print new_class.age  # 24
    print new_class.name  # xb
    # print new_class.personal_information(65) # ERROR
    new_class.ID = 65
    print new_class.ID  # 65
