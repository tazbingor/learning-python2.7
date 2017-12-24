#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/23 下午7:00
# @Author  : Aries
# @Site    : 
# @File    : py115_custom_class.py
# @Software: PyCharm
'''
13-3. 对类进行定制。写一个类，用来将浮点数值转换为金额。在本练习里，我们使用美国
货币，但读者也可以自选任意货币。

基本任务:
    编写一个dollarize()函数，它以一个浮点数值作为输入，返回一个字符串形式的
金额数。比如说：
dollarize(1234567.8901) ==> ‘$1,234,567.89.
dollarize()返回的金额数里应该允许有逗号(比如1,000,000)，和美元的货币符号。如果有负
号，它必须出现在美元符号的左边。完成这项工作后，你就可以把它转换成一个有用的类，名为
MoneyFmt。
    MoneyFmt 类里只有一个数据值(即，金额)，和五个方法(你可以随意编写其他方法)。__init__()
构造器对数据进行初始化，update()方法把数据值替换成一个新值，__nonzero__()是布尔型的，当
数据值非零时返回True，__repr__()方法以浮点数的形式返回金额；而__str__()方法采用和
dollarize()一样的字符格式显示该值。

(a) 编写update()方法，以实现数据值的修改功能。
(b) 以你已经编写的 dollarize()的代码为基础，编写__str__()方法的代码
(c) 纠正__nonzero__()方法中的错误，这个错误认为所有小于1 的数值，例如，50 美分($0.50)，
返回假值(False)。
(d) 附加题: 允许用户通过一个可选参数指定是把负数数值显示在一对尖括号里还是显示一个
负号。默认参数是使用标准的负号
'''


class MoneyFmt(object):
    def __init__(self, value=0.0):
        self.__data_init(value)

    def update(self, value=None):
        if value != None:
            self.__data_init(value)
        else:
            print 'Value has not been updated.'

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


if __name__ == '__main__':
    money_fmt = MoneyFmt(1234567.8901)
    print money_fmt.dollarize()
    print money_fmt
    money_fmt.update(-0.3)
    print money_fmt

    print money_fmt.__nonzero__()  # False
