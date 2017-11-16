#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/15 上午4:25
# @Author  : Aries
# @Site    : 
# @File    : py033_idcheck.py
# @Software: PyCharm
'''
检测字符串
'''

import string

alphas = string.letters + '_'
nums = string.digits

print '欢迎使用标识符检测1.0'
print '输入长度大于1'
myInput = raw_input('输入标识符进行测试:\n')

if len(myInput) > 1:
    if myInput[0] not in alphas:  # 检测首字符是否为字母
        print '无效输入:第一个字符必须是字母'

    else:
        for otherChar in myInput[1:]:  # 从第二个字符到最后一个字符的循环
            if otherChar not in alphas + nums:
                print '无效输入:剩余的字符必须是字母'
                break
        else:
            print '此标识符合法'
