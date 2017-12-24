#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/24 上午11:24
# @Author  : Aries
# @Site    : 
# @File    : py118_geometry_02.py
# @Software: PyCharm
'''
13-6 几何。
创建一个直线/直线段类。除主要的数据属性：一对坐标值（参见上一个练习）外，它还具有长度和斜线属性。
你需要覆盖__repr__()方法（如果需要的话，还有__str__()方法），使得代表那条直线（或直线段）的字符串表示形式是由一对元组构成的元组，
即（(x1，y1)、(x2，y2)）。
总结：
    __repr__()    将直线的两个端点（始点和止点）显示成一对元组
    length        返回此线段的长度 - 不要使用“len”，因为这样使人误解它是整型。
    slope        返回此线段值线段的斜率（或在适当的时候返回None）
'''


class LineSegment(object):
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return "((%d,%d),(%d,%d))" % (self.x1, self.y1, self.x2, self.y2)

    __repr__ = __str__

    def length(self):
        '''计算两点间的长度'''
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5

    def slope(self):
        '''计算斜率'''
        if self.x1 != self.x2:
            return (self.y2 - self.y1) // (self.x2 - self.x1)
        return None


if __name__ == '__main__':
    ls = LineSegment(1, 2, 3, 4)
    print ls.__repr__()  # ((1, 2), (3, 4))
    print round(ls.length(), 2)  # 2.83
    print ls.slope()  # 1
