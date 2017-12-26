#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/25 下午10:18
# @Author  : Aries
# @Site    : 
# @File    : py123_shopping.py
# @Software: PyCharm
'''
13-11. 电子商务。
你需要为一家B2C（企业到消费者）零售商编写一个基础的电子商务引擎。
你需要写一个针对顾客的类User，
一个对应存货清单的类Item，
还有一个对应购物车的类叫Cart。
货物放到购物车里，顾客可以有多个购物车。同时购物车里可以有多个货物，包括多个同样的货物。
'''


class User(object):
    def __init__(self, name='Admin', id=0, **carts):
        self.username = name
        self.id = id
        for (key, value) in carts.itervalues():
            if hasattr(self, key):
                setattr(self, key, value)


class Item(object):
    def __init__(self, **kwargs):
        for (key, value) in kwargs.itervalues():
            if hasattr(self, key):
                setattr(self, key, value)


class Cart(object):
    def __init__(self, **kwargs):
        for (key, value) in kwargs.itervalues():
            if hasattr(self, key):
                setattr(self, key, value)


if __name__ == '__main__':
    user_01 = User('张三', 1)
    user_02 = User('李四', 2)
