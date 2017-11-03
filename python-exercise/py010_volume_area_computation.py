#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/3 下午2:43
# @Author  : Aries
# @Site    : 
# @File    : py010_volume_area_computation.py
# @Software: PyCharm
'''
体积和面积的计算
正方形,立方体,圆形,球体
'''
import math

square_side = int(raw_input("求正方形面积,请输入其边长:\n"))
cube_side = int(raw_input("求立方体表面积和体积,请输入其边长:\n"))
radius = int(raw_input("求圆形面积,请输入其半径:\n"))
sphere_radius = int(raw_input("求球体表面积和体积,请输入其半径:\n"))
print "正方形的面积为:%s" % str(int(square_side ** 2))
print "立方体的表面积为:%s" % str(int(square_side ** 3))
print "立方体的体积为:%s" % str(int(square_side ** 3))
print "圆形的面积为:%s" % str(int(math.pi * radius ** 2))
print "球体的表面积为:%s" % str(int(4 * math.pi * sphere_radius ** 2))
print "球体的体积为:%s" % str(int(4 / 3 * math.pi * sphere_radius ** 3))
