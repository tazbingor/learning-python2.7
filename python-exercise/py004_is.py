#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/2 下午3:27
# @Author  : Aries
# @Site    : 
# @File    : py004_is.py
# @Software: PyCharm

'''
a is b,c is d,e is f分别输出什么?
'''
a = 10

b = 10

c = 100

d = 100

e = 100.0

f = 100.0

print a is b  # True
print c is d  # True
print e is f  # True

# 都为True,原因很简单,首先数字类型是属于不可改变的类型,
# 所以当一个或者多个数字变量的值相同,那么在实例化时,这些变量会指向同一块内存区域 使用id()即可证明
print id(a) == id(b)  # True
print id(c) == id(d)  # True
print id(e) == id(f)  # True
