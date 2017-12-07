#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/7 下午5:26
# @Author  : Aries
# @Site    : 
# @File    : py071_reduce.py
# @Software: PyCharm
'''
reduce()
reduce() 函数会对参数序列中元素进行累积。
函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给reduce中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

'''


# reduce实现
def myReduce(bin_func, seq, init=None):
    lseq = list(seq)
    if init is None:
        res = lseq.pop(0)
    else:
        res = init
    for item in lseq:
        res = bin_func(res, item)
    return res
