#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/25 下午9:26
# @Author  : Aries
# @Site    : 
# @File    : py122_array.py
# @Software: PyCharm
'''
13-10. 堆栈和队列。编写一个类，定义一个能够同时具有堆栈（）和队列（）操作行为的数据结构。
这个类和Perl语言中的数组相像。需要实现四个方法：
    shift()    返回并删除列表中的第一个元素，类似于前面的dequeue()函数。
    unshift() 在列表的头部“压入”一个新元素。
    push() 在列表的尾部加上一个新元素，类似于前面的enqueue()和push()方法。
    pop() 返回并删除列表中的最后一个元素，与前面的pop()方法完全一样
'''


class Array(object):
    def __init__(self, alist):
        self.array_list = list(alist)

    def __isempty(self):
        if len(self.array_list) == 0:
            return True
        return False

    def shift(self):
        # if not self.__isempty():
        if not self.array_list:
            element = self.array_list[0]
            del self.array_list[0]
            return element
        else:
            raise Exception('该集合为空,不能执行此操作!')

    def unshift(self, element=None):
        self.array_list.insert(0, element)

    def push(self, element=None):
        self.array_list.append(element)

    def pop(self):
        # if not self.__isempty():
        if not self.array_list:
            index = len(self.array_list) - 1
            element = self.array_list[index]
            del self.array_list[index]
            return element
        else:
            raise Exception('该集合为空,不能执行此操作!')

    def __str__(self):
        return str(self.array_list)

    __repr__ = __str__


if __name__ == '__main__':
    temp_list = [0, 1, 2, 3, 4, 5]
    array = Array(temp_list)
    array.push(6)
    print array  # [0, 1, 2, 3, 4, 5, 6]

    array.pop()
    print array  # [0, 1, 2, 3, 4, 5]

    array.unshift(7)
    print array  # [7, 0, 1, 2, 3, 4, 5]
