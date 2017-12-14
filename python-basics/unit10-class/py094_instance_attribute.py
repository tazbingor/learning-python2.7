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
        daily = round((self.roomRate * (1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily


if __name__ == '__main__':
    sfo = HotelRoomCalc(299)
    print sfo.calcTotal()  # 354.31
    print sfo.calcTotal(2)  # 708.62

    sea = HotelRoomCalc(189, 0.086, 0.058)
    print sea.calcTotal()  # 216.22
    print sea.calcTotal(4)  # 864.88

    waswkday = HotelRoomCalc(169, 0.045, 0.02)  # 新实例
    waswkEnd = HotelRoomCalc(119, 0.045, 0.02)  # 新实例
    print waswkday.calcTotal(5) + waswkEnd.calcTotal()  # 七天的租金 1026.63
