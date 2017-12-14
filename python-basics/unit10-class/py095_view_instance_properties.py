#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/15 上午5:13
# @Author  : Aries
# @Site    :
# @File    : py095_view_instance_properties.py
# @Software: PyCharm
'''
查看实例属性

__dict__属性由字典构成,包含一个实例的所有属性.
key是属性名,value是属性的对应数据,__dict__中仅有实例属性,没有类属性和特殊属性
'''


class Test(object):
    pass


class Student(object):
    pass


if __name__ == '__main__':
    test = Test()
    test.car = 'BMW'
    test.watch = 'TAG HEUER MONACO'

    stu = Student()

    # dir打印实例所有属性
    print dir(test)
    print dir(stu)

    # __dict__打印自定义的属性返回一个字典
    print test.__dict__  # {'car': 'BMW', 'watch': 'TAG HEUER MONACO'}
    print stu.__dict__  # {}

    # __class__ 查看实例化的类
    print test.__class__  # <class '__main__.Test'>
    print stu.__class__  # <class '__main__.Student'>
