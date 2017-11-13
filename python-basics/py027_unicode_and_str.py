#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/13 下午4:10
# @Author  : Aries
# @Site    : 
# @File    : py027_unicode_and_str.py
# @Software: PyCharm
'''
str() 与 unicode
'''

print isinstance(u'\0xAB', str)  # False
print not isinstance('foo', unicode)  # True
print isinstance('', basestring)  # True
print not isinstance('foo', basestring)  # False
print
'''
关于basestring
basestring() 方法是 str 和 unicode 的超类（父类），也是抽象类，因此不能被调用和实例化，
但可以被用来判断一个对象是否为 str 或者 unicode 的实例，isinstance(obj, basestring) 等价于 isinstance(obj, (str, unicode))。

'''

str_unicode = u'python'
print type(str_unicode)  # <type 'unicode'>
str1 = str(str_unicode)  # <type 'str'>
print type(str1)
