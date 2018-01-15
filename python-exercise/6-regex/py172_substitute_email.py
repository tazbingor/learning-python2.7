#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午8:36
# @Author  : Aries
# @Site    : 
# @File    : py172_substitute_email.py
# @Software: PyCharm
'''
15-26.将每行中的电子邮件地址替换为你自己的电子邮件地址。
'''
import re

email = 'test@yahoo.jp'


def sub_email(path, email=''):
    ls = []
    with open(path) as f:
        for line in f:
            ls.append(re.sub('\w+@.+::', email + '::', line))

    with open(path, 'w') as f:
        f.write(''.join(ls))


if __name__ == '__main__':
    sub_email(r'redata.txt', 'python@yahoo.com')
