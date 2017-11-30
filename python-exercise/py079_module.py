#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/30 下午6:17
# @Author  : Aries
# @Site    : 
# @File    : py079_module.py
# @Software: PyCharm
'''
9-8模块研究
提取模块的属性资料.提示用户输入一个模块名.然后使用dir()和其他函数提取模块属性,显示它们的名字,类型,值
'''


def module_details(strModule):
    modules = __import__(strModule)
    mod = dir(modules)
    # print mod
    names = []
    mtypes = []
    values = []
    for i in mod:
        names.append(i)
        mtypes.append(type(getattr(mod, i)))
        values.append(getattr(mod, i))
    return [names, mtypes, values]


user_input = raw_input('请输入模块名:\n')
mod_results = module_details(user_input)
print '模块名: ', mod_results[0]
print '类型为: ', mod_results[1]
print '值为: ', mod_results[2]
