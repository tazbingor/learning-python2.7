#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/24 上午11:17
# @Author  : Aries
# @Site    : 
# @File    : py117_coordinates.py
# @Software: PyCharm
'''
几何。建立一个由有序数值对（x，y）组成的Point类，它代表某个点的X坐标和Y坐标。
X坐标和Y坐标在实例时被传递给构造器，如果没有给出他们的值，则默认为坐标的原点。
'''


class Point(object):
    def __init__(self, x=0, y=0):
        self.point_x = x
        self.point_y = y

    def __str__(self):
        return 'x:%d y:%d' % (self.point_x, self.point_y)


if __name__ == '__main__':
    point = Point()
    print point  # x:0 y:0

    point2 = Point(1, 2)
    print point2  # x:1 y:2
