#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/14 下午7:22
# @Author  : Aries
# @Site    : 
# @File    : py094_instance_attribute.py
# @Software: PyCharm
'''
实例属性
'''


# 使用缺省数进行实例化
class HotelRoomCalc(object):
    def __init__(self, rt, sales=0.085, rm=0.1):
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        daily = round((self.roomRate(1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily


if __name__ == '__main__':
    sfo = HotelRoomCalc(299)
    print sfo.calcTotal()
