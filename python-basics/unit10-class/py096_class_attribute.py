#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/15 上午5:43
# @Author  : Aries
# @Site    : 
# @File    : py096_class_attribute.py
# @Software: PyCharm
'''
访问类属性

1. 倘若直接改变类属性,那么所有此类的实例都会被影响
2. 通俗的说,类是模子,实例是模子造的东西,若模子本身改变,那么实例也不会幸免(类的持久性)

python核心编程: 当一个实例在类属性被修改后才创建,那么更新的值将生效.类属性的修改会影响所有的实例

换个思路,
1. 要修改类属性的时候,要使用类名
2. 谨慎使用
'''


class Test(object):
    version = 1.2


if __name__ == '__main__':
    v = Test()
    v1 = Test()  # 倘若再创造一个实例
    # 通过实例访问
    print v.version  # 1.2
    print v1.version
    # 直接通过类访问
    print Test.version  # 1.2
    print'-' * 50

    # 通过类,也只能通过类来更新数据
    Test.version += 1
    print v.version  # 被改变
    print Test.version
    print v1.version
    print'-' * 50

    # 改变v的类属性值
    v.version += 1
    print v.version  # 3.2
    print Test.version  # 2.2
    print v1.version  # 2.2
