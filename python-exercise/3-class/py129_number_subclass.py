#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/27 下午6:28
# @Author  : Aries
# @Site    : 
# @File    : py129_number_subclass.py
# @Software: PyCharm
'''
13-17 数值类型子类化。
在示例13.3中所看到的moneyfmt.py脚本基础上修改它，使得它可以扩展Python的浮点类型。
请确保它支持所有操作，而且是不可变的。
'''


class MoneyFmt(object, float):
    def __init__(self, value=0.0):
        self.__data_init(value)

    # def update(self, value=None):
    #     if value != None:
    #         self.__data_init(value)
    #     else:
    #         print 'Value has not been updated.'

    def __data_init(self, value=0.0):
        self.money = float(value)
        self.round_money = round(self.money, 2)
        self.str_money = str(self.round_money)
        self.dollar = self.str_money.split('.')[0]
        self.cent = self.str_money.split('.')[1]

    # __repr__ = __str__

    def dollarize(self):
        abs_money = abs(self.round_money)
        temp_dollar = '{:,}'.format(abs_money)
        str_dollar = ''.join(('$', temp_dollar))
        if self.money > 0:
            return str_dollar
        else:
            return '-' + str_dollar

    def get_dollar(self):
        return self.dollar

    def get_cent(self):
        return str('0.', self.cent)

    def __nonzero__(self):
        if self.money < 1:
            return False
        else:
            return True

    def __str__(self):
        return self.dollarize()

    def __repr__(self):
        return self.money
