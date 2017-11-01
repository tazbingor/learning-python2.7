#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/1 下午3:48
# @Author  : Aries
# @Site    : 
# @File    : py008_object.py
# @Software: PyCharm
# python 对象

"""
python对象
首先,万物皆对象,java,js,ruby等语言都是如此

python对象的三个特点
1. 每个对象都有一个唯一id,这个id可以被认为是每个对象的内存地址
2. 每个对象都有一个类型,可以用type()查看python的对象
3. 对象所表示的值
"""

import dis

# 每个对象都有唯一id
a = 1
b = 1
c = 1
print 'a:' + str(id(a)) + ' b:' + str(id(b)) + ' c:' + str(id(c))  # 三个值得id相同
# 因为python以数据最为主导,上述a,b,c三个变量相同,是调用数值'1'的内存,所以三个变量的id相同
a = 1
b = 1.0
print 'a:' + str(id(a)) + ' b:' + str(id(b))  # 不相同,因为b为浮点数


def functionA():
    return 1


def functionB():
    return 1


print 'functionA:' + str(id(functionA())) + ' functionB:' + str(id(functionB()))
print str(id(functionA())) == str(id(functionB()))  # True
print 'functionA的类型为:' + str(type(functionA()))
print 'functionB的类型为:' + str(type(functionB()))
3


# 若都是空函数
def functionC():
    pass


def functionD():
    pass


print 'functionC:' + str(id(functionC())) + ' functionD:' + str(id(functionD()))
print str(id(functionC())) == str(id(functionD()))  # True
print 'functionC的类型为:' + str(type(functionC()))  # <type 'NoneType'>
print 'functionD的类型为:' + str(type(functionD()))  # <type 'NoneType'>


# 若是空类
class A:
    pass


class B:
    pass


print 'A:' + str(id(A)) + ' B:' + str(id(B))
print str(id(A)) == str(id(B))  # False
print 'A的类型为:' + str(type(A))  # <type 'classobj'>
print 'B的类型为:' + str(type(B))  # <type 'classobj'>
print str(dis.dis(A))
print str(dis.dis(B))
