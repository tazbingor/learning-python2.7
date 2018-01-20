#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/14 下午7:05
# @Author  : Aries
# @Site    : 
# @File    : py011_list_queue.py
# @Software: PyCharm
'''
列表模拟队列

从末尾进,从开头出,相当于超市排队
实现以下功能
1. 后端插入
2. 前端弹出,返回队顶元素
3. 队列长度
4. 展示队列

'''
myListQueue = ['1', '2', '3']


# 后端插入元素
def push():
    global myListQueue

    myListQueue.append(raw_input('请输入你要添加的字符串:\n').strip())
    # print myListQueue


def pop():
    if len(myListQueue) == 0:
        print '队列为空,请向队列中添加新的元素'
    else:
        print '元素[', popit(), ']从该列表中弹出'


def popit():
    global myListQueue
    arr = list(myListQueue)
    result = arr[0]
    arr.remove(arr[0])
    myListQueue = arr
    # print myListQueue
    return result


def showQueue():
    print myListQueue


print '-' * 50
showQueue()
push()
showQueue()
pop()
showQueue()
