#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/24 上午11:57
# @Author  : Aries
# @Site    : 
# @File    : py119_data.py
# @Software: PyCharm
'''
13-7 数据类。
提供一个time模块的接口，允许用户按照自己给定时间的格式，
比如：“MM/DD/YY”、“MM/DD/YYYY”、“DD/MM/YY”、“DD/MM/YYYY”、
“Mon DD, YYYY”或是标准的Unix日期格式“Day Mon DD, HH:MM:SS YYYY”来查看日期。
你的类应该维护一个日期值，并用给定的时间创建一个实例。
如果没有给出时间值，程序执行时会默认采用当前的系统时间。还包括另外一些方法。
update()    按照给定时间或是默认的当前系统时间修改数据值
display()    以代表时间格式的字符串做参数，并按照给定时间的格式显示：

    'MDY' -> MM/DD/YY
    'MDYY'-> MM/DD/YYYY
    'DMY' -> DD/MM/YY
    'DMYY' -> DD/MM/YYYY
    'MODYY' -> Mon DD, YYYY
如果没有提供任何时间格式，默认使用系统时间或ctime()的格式。附加题：把这个类和练习6-15结合起来。
'''
import time


class MyTime(object):
    dispplay_tuple = (
        '1,Mon DD, YYYY',
        '2,MM/DD/YYYY',
        '3,DD/MM/YY',
        '4,DD/MM/YYYY',
        '5,DD/MM/YYYY'
    )

    __dispplay_mode = {
        'MDY': '%m-%d-%y',
        'MDYY': '%m-%d-%y',
        'DMY': '%d-%m-%y',
        'DMYY': '%d-%m-%y',
        'MODYY': '%b %d,%y'
    }

    def __init__(self, value=time.time()):
        self.time_val = value
        # self.display_mode = display_mode

    def update(self, value=time.time()):
        self.time_val = value
        # self.display_mode = display_mode

    def display(self, mode=dispplay_tuple[0]):
        time_val = ''
        if mode != self.dispplay_tuple[0]:
            mt = time.localtime(self.time_val)
            time_val = time.strftime(self.__dispplay_mode[mode], mt)
        else:
            time_val = time.ctime()

        return time_val


if __name__ == '__main__':
    tm = MyTime()
    for each in tm.dispplay_tuple:
        print each
    user_input = int(raw_input('请选择时间显示格式:\n'))

    print tm.display(tm.dispplay_tuple[user_input - 1])
