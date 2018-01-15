#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/15 下午8:00
# @Author  : Aries
# @Site    : 
# @File    : py163_match_redata.py
# @Software: PyCharm
'''
15-17.统计生成的redata.txt文件中，星期中的每一天出现的次数（或统计各月份出现的次数）。
'''
import re

week = {}.fromkeys(('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'), 0)
st = '^(' + '|'.join(week.keys()) + ')'


def get_week(path=''):
    with open(path) as f:
        for line in f:
            m = re.match(st, line)
            if m is not None:
                week[m.group()] += 1
    return week


if __name__ == '__main__':
    print get_week('redata.txt')
    # {'Wed': 1, 'Sun': 0, 'Fri': 0, 'Tue': 0, 'Mon': 0, 'Thu': 0, 'Sat': 0}
