#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/8 下午5:24
# @Author  : Aries
# @Site    : 
# @File    : py103_functional_map.py
# @Software: PyCharm
'''
11–7. 用map() 进行函数式编程。
给定一对同一大小的列表， 如[1， 2， 3] 和['abc','def','ghi',....]，将两个标归并为一个由每个列表元素组成的元组的单一的表，
以使我们的结果看起来像这样：{[(1, 'abc'), (2, 'def'), (3, 'ghi'), ...}.
（虽然这问题在本质上和第六章的一个问题相似，那时两个解没有直接的联系）然后创建用zip 内建函数创建另一个解。
'''
newdict = lambda list1, list2: map(None, list1, list2)

newzip = lambda list1, list2: zip(list1, list2)

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = ['abc', 'def', 'ghi']
    print newdict(list1, list2)  # [(1, 'abc'), (2, 'def'), (3, 'ghi')]

    print newzip(list1, list2)  # [(1, 'abc'), (2, 'def'), (3, 'ghi')]
