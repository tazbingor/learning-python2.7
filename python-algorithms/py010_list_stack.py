#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/14 下午5:42
# @Author  : Aries
# @Site    : 
# @File    : py010_list_stack.py
# @Software: PyCharm
'''
简易的列表模拟堆栈
(不使用类进行编码)

什么是堆栈?
对列特点：先进先出、后进后出,如同子弹按到弹夹一样
那么,堆栈会有两种操作
1.压栈
2.弹栈


other :
pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
'''

myListStack = ['1', '2', '3']


# 弹栈
def popit():
    if len(myListStack) == 0:
        print '该列表为空,请添加新的字符串元素!'
    else:
        print '删除了[', [myListStack.pop()], ']元素'


# 压栈
def pushit():
    myListStack.append(raw_input('请输入你要添加的字符串:\n').strip())


def showStack():
    print myListStack


print '-' * 50
showStack()
pushit()
showStack()
popit()
showStack()
