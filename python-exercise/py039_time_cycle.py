#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/16 下午10:51
# @Author  : Aries
# @Site    : 
# @File    : py039_time_cycle.py
# @Software: PyCharm
'''
时间转换

转换。为练习5-13写一个姊妹函数，接受分钟数，返回小时数和分钟数。总时间不变，并且要求小时尽可能大。
'''


def getTimeCycle(min):
    if min / 60 != 0:
        return '%s分钟是:%s小时%s分钟' % (str(min), str(min / 60), str(min % 60))


user_input = int(raw_input('请输入分钟:\n'))
print getTimeCycle(user_input)

