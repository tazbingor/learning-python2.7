#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/25 下午8:47
# @Author  : Aries
# @Site    : 
# @File    : py121_queue.py
# @Software: PyCharm
'''
13-9. 队列类。
一个队列（queue）是一种具有先进先出（first-in-first-out，FIFO）特性的数据结构。
一个队列就像是一行队伍，数据从前端被移除，从后端被加入。
。这个类必须支持下面几种方法：
    enqueue()在列表的尾部加入一个新的元素。
    dequeue()在列表的头部取出一个元素，返回它并且把它从列表中删除。请参见上面的练习和示例6.3。
'''


class MyQueue(object):
    def __int__(self, queue_list):
        """

        :type queue_list: list
        """
        self.queue_list = queue_list

    def enqueue(self, element=None):
        self.queue_list.append(element)

    def dequeue(self):
        if self.isempty():
            element = self.queue_list[0]
            del self.queue_list
            return element
        else:
            raise Exception('该队列为空,不能执行此操作!')

    def isempty(self):
        if len(self.queue_list) == 0:
            return True
        return False

    def __str__(self):
        return str(self.queue_list)

    __repr__ = __str__


if __name__ == '__main__':
    temp_list = [0, 1, 2, 3, 4, 5]
    queue = MyQueue(temp_list)
    print queue
