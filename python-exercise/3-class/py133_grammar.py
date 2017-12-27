#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/27 下午7:56
# @Author  : Aries
# @Site    : 
# @File    : py133_grammar.py
# @Software: PyCharm
'''
13-21 .装饰符和函数调用语法
我们使用一个装饰函数把x转化成一个属性对象,但由于装饰符是Python2.4才有的新功能,我们给出了另一个适用于旧版本的语法:
    X = property(**x())
此执行语句时到底发生了什么?
为什么它与装饰符等价?
'''

'''
首先property是一个类，其作用是用来包装类的属性，
这个属性可以根据实际需要，控制是否可读(设置fget参数)、可写(设置fset参数)、可删除(设置fdel参数)。
其实,实际上property()是特殊的attribute，
可以自定义 getter/setter/deleter 等属性，自己控制 get/set/delete 时触发的方法
**x() 代表了多种属性,所以property()与@property等价
'''
