#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/6 下午7:20
# @Author  : Aries
# @Site    : 
# @File    : py058_parameter_set.py
# @Software: PyCharm
'''
参数组
    1.python 允许程序员执行一个没有显示定义参数的函数,通过把一个tuple(非关键字参数)或dict(关键字参数)作为参数传递给函数
'''


def test(*tuple_grp_nonkw_args, **dict_grp_kw_args):
    return [type(tuple_grp_nonkw_args), type(dict_grp_kw_args), tuple_grp_nonkw_args, dict_grp_kw_args]


if __name__ == '__main__':
    list1 = test(1, 2)
    print list1[0]  # <type 'tuple'>
    print list1[1]  # <type 'dict'>
    print list1[2]
    print list1[3]
    print '-' * 50
    list2 = test([1, 2, 3], {1: '1', 2: '2', 3: '3'})
    print list2[0]  # <type 'tuple'>
    print list2[1]  # <type 'dict'>
    print list2[2]
    print list2[3]
    print '-' * 50
    list3 = test(1, 2, 3, **{'1': 1, '2': 2, '3': 3})
    print list3[0]  # <type 'tuple'>
    print list3[1]  # <type 'dict'>
    print list3[2]  # (1, 2, 3)
    print list3[3]  #
    print '-' * 50
    list4 = test(1, 2, 3, '4', '5')
    for i in list4:
        print i, ':', type(i)
    print '-' * 50
    list5 = test(1, 2, 3, a='4', b='5')
    for i in list5:
        print i, ':', type(i)