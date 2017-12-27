#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/27 下午7:48
# @Author  : Aries
# @Site    : 
# @File    : py132_class_of_custom.py
# @Software: PyCharm
'''
13-20.类的定制。改进脚本time60.py
(a)允许“空”实例化：如果小时和分钟的值没有给出，默认为0小时0分钟。
(b)用0占位组成两位数的形式，因为当前的时间格式不符合要求。
(c)除了用hours(hr)和minutes(min)进行初始化外，还支持以下时间输入格式：
一个由小时和分钟组成的元组，如(10,30)
一个由小时和分钟组成的字典，如{'hr':10, 'min':30}
一个代表小时和分钟的字符串，如"10:30"
(e)实现__repr__()。
(f)添加60进制的运算功能。
'''


class Time60(object):
    def __init__(self, hr=0, min=0):
        if isinstance(hr, str):
            tmp = hr.split(':')
            self.hr = int(tmp[0])
            self.min = int(tmp[1])
        else:
            self.hr = hr
            self.min = min

    def __str__(self):
        return '%d:%d' % (self.hr, self.min)

    __repr__ = __str__

    # 加法
    # def __add__(self, other):
    #     return self.__class__(self.hr + other.hr,
    #                           self.min + other.min)
    def __add__(self, other):
        hr = self.hr + other.hr
        min = self.min + other.min
        ahr = min // 60
        min %= 60
        hr += ahr
        return self.__class__(hr, min)

    # 原位加法
    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self


if __name__ == '__main__':
    mon = Time60(10, 30)
    tue = Time60(11, 15)
    print mon + tue  # 21:45
    print mon  # 10:30
    print tue  # 11:15

    print Time60(*(10, 30))  # 10:30
    print Time60(**{'hr': 10, 'min': 30})  # 10:30
