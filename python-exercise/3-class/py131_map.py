#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/27 下午6:35
# @Author  : Aries
# @Site    : 
# @File    : py131_map.py
# @Software: PyCharm
'''
13-19. 映射类型子类化。
'''


class Test(dict, object):
    def keys(self):
        return sorted(super(Test, self).keys())


if __name__ == '__main__':
    temp_dict = Test((('C', 3), ('B', 2), ('A', 1)))
    print [key for key in temp_dict]  # ['A', 'C', 'B']
    print temp_dict.keys()  # ['A', 'B', 'C']

'''
a.当方法key调用会报错(超出递归深度)
b.此写法相当于递归,需要通过类继承dict,并同时使keys函数返回Test的映射(super(Test,self))
'''
