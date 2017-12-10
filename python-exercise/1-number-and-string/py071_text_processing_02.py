#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 下午6:15
# @Author  : Aries
# @Site    : 
# @File    : py071_text_processing_02.py
# @Software: PyCharm
'''
8-10 文本处理. 要求输入一个姓名列表,输入格式是"LastName,FirstName",即姓 逗号 名.编写程序处理输入,
如果用户输入错误,比如"FirstName LastName,",请纠正这些错误,并通 知用户.同时你还需要记录输入错误次数.
当用户输入结束后,给列表排序,然后以"姓,名"的顺序显示. 输入输出示例(你不需要完全按照这里的例子完成):
'''


def name(num):
    count = 0
    result = []
    for i in range(num):
        print 'Please enter name %d:' % i,
        n_ame = raw_input()
        if ',' in n_ame:
            result.append(n_ame)
        else:
            count += 1
            print 'Wrong format...should be Last,First.'
            print 'You have done this %d time(s) already.Fixing input...' % count
            n_ame = n_ame.split()
            # print n_ame
            result.append(n_ame[1] + ',' + n_ame[0])

    return sorted(result)


num = input('Enter total number of names:')
n_ame = name(num)
for i in n_ame:
    print i
