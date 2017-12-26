#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/26 下午4:06
# @Author  : Aries
# @Site    : 
# @File    : py125_trading_system.py
# @Software: PyCharm
'''
13-13. 股票投资组合类。
你的数据库中记录了每个公司的名字、股票代码、购买日期、购买价格和持股数量。
需要编写的方法包括：
    添加新代号、
    删除代号、
    年回报率。
'''


class Stock(object):
    def __init__(self, name, sid, date, price, count):
        self.stock_name = name
        self.stock_id = sid
        self.purchase_date = date
        self.price = price
        self.stock_count = count

    def __str__(self):
        return '%s %d %s %.2f %d' \
               % (self.stock_name, self.stock_id,
                  self.purchase_date, self.price, self.stock_count)


class StockOperation(object):
    def __init__(self, stock_obj=None):
        self.__stock_db = []
        self.profit = 0.0
        # self.stock = stock_obj

    def add_stock(self, stock_obj):
        self.__stock_db.append(stock_obj)

    def delete_stock(self):
        temp_list = []
        for item in self.__stock_db:
            if item.stock_count != 0:
                temp_list.append(item)
        self.__stock_db = temp_list

    def sub(self, name, subnum):
        for item in self.__stock_db:
            if item[0].name == name:
                item[3] -= subnum
                self.profit = (item[0].price - item[1]) * subnum + self.profit
                return self.profit
        return 0

    def view_stock(self):
        return self.__stock_db


if __name__ == '__main__':
    mystock = Stock('五宝钢铁', 600119, '2017/12/25 10.25', 8.36, 10000)
    mystock1 = Stock('四宝钢铁', 600120, '2017/12/20 10.25', 7.36, 10000)
    mystock2 = Stock('三宝钢铁', 600121, '2017/12/19 10.25', 9.36, 0)

    print mystock
    print mystock1
    print mystock2
    # add
    sto = StockOperation()
    sto.add_stock(mystock)
    sto.add_stock(mystock1)
    sto.add_stock(mystock2)
    # print sto.view_stock()
    for i in sto.view_stock():
        print i
        print type(i)

    # delete
    sto.delete_stock()
    for i in sto.view_stock():
        print i
