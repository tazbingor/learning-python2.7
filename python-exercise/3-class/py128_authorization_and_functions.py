#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/27 下午5:59
# @Author  : Aries
# @Site    : 
# @File    : py128_authorization_and_functions.py
# @Software: PyCharm
'''
13-16.授权和函数编程。
(a)请为示例中的CanOpen类编写一个writelines()方法，这个新函数可以一次读入多行文本，然后将文本转化为大写的形式。
(b)在writelines()方法中添加一个参数，用这个参数来指明是否需要为每行文本加上一个换行符。此参数的默认值是False，表示不加换行符
'''


class CapOpen(object):
    def __init__(self, file_path, opt='r', buf=-1):
        self.file = open(file_path, opt, buf)

    def __str__(self):
        return str(self.file)

    __repr__ = __str__

    def write(self, line):
        self.file.write(line.upper())

    def writelines(self, str_list, word_wrap=False):
        for item in str_list:
            if word_wrap:
                item += '\n'
            self.file.write(item.upper())

    def __getattr__(self, item):
        return getattr(self.file, item)


if __name__ == '__main__':
    str_list = [
        'def __str__(self):',
        'return str(self.file)'
    ]
    capopen = CapOpen('test.txt', 'wb')
    capopen.writelines(str_list)
