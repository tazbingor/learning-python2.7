#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/25 下午8:16
# @Author  : Aries
# @Site    : 
# @File    : py120_stack.py
# @Software: PyCharm
'''
13-8 堆栈类。一个堆栈（stack）是一种具有后进先出（last-in-first-out，LIFO）特性的数据结构。
我们可以把它想象成一个餐盘架。最先放上去的盘子将是最后一个取下来的，而最后一个放上去的盘子是最先被取下来的。
你的类中应该有push()方法（向堆栈中压入一个数据项）和pop()方法（从堆栈中移出一个数据项）。
还有一个叫isempty()的布尔方法。如果堆栈是空的，返回布尔值1，否则返回0；
一个名叫peek()的方法，取出堆栈顶部的数据项，但并不移除它。
注意，如果你使用一个列表来实现堆栈，那么pop()方法从Python1.5.2版本起已经存在了。
那就在你编写的新类里，加上一段代码检查pop()方法是否已经存在。
如果经检查pop()方法存在，就调用这个内建的方法；否则就执行你自己编写的pop()方法。
你很可能要用到列表对象；如果用到它时，不需要担心实现列表的功能（例如切片）。
只要保证你写的堆栈类能够正确实现上面的两项功能就可以了。你可以用列表对象的子类或自己写个类似列表的对象，请参考示例6.2。


'''


class Stack(object):
    def __init__(self, alist):
        self.stack_list = list(alist)

    def push(self, element=None):
        self.stack_list.insert(0, element)

    def mypop(self):
        if self.isempty() == 0:
            del self.stack_list[0]
        else:
            raise Exception('该堆栈为空!')

    def peek(self):
        return self.stack_list[0]

    def isempty(self):
        if len(self.stack_list) == 0:
            return 1
        return 0

    def __str__(self):
        return str(self.stack_list)

    __repr__ = __str__


if __name__ == '__main__':
    alist = [0, 1, 2, 3, 4, 5]
    stack = Stack(alist)
    print stack  # [0, 1, 2, 3, 4, 5]

    stack.push(6)
    print stack  # [6, 0, 1, 2, 3, 4, 5]

    stack.mypop()
    print stack  # [0, 1, 2, 3, 4, 5]
    print stack.peek()  # 0
    print stack  # [0, 1, 2, 3, 4, 5]

    print stack.isempty()  # 0
