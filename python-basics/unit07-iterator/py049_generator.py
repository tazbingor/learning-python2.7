#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/22 下午12:02
# @Author  : Aries
# @Site    : 
# @File    : py049_generator.py
# @Software: PyCharm

'''
生成器

首先请确信，生成器就是一种迭代器。生成器拥有next方法并且行为与迭代器完全相同，这意味着生成器也可以用于Python的for循环中。
另外，对于生成器的特殊语法支持使得编写一个生成器比自定义一个常规的迭代器要简单不少，所以生成器也是最常用到的特性之一。
从Python 2.5开始，[PEP 342：通过增强生成器实现协同程序]的实现为生成器加入了更多的特性，这意味着生成器还可以完成更多的工作。

生成器特点:
1. 调用生成器函数将返回一个生成器；
2. 第一次调用生成器的next方法时，生成器才开始执行生成器函数（而不是构建生成器时），直到遇到yield时暂停执行（挂起），并且yield的参数将作为此次next方法的返回值；
3.之后每次调用生成器的next方法，生成器将从上次暂停执行的位置恢复执行生成器函数，直到再次遇到yield时暂停，并且同样的，yield的参数将作为next方法的返回值；
4. 如果当调用next方法时生成器函数结束（遇到空的return语句或是到达函数体末尾），则这次next方法的调用将抛出StopIteration异常（即for循环的终止条件）；
5. 生成器函数在每次暂停执行时，函数体内的所有变量都将被封存(freeze)在生成器中，并将在恢复执行时还原，并且类似于闭包，即使是同一个生成器函数返回的生成器，封存的变量也是互相独立的。
'''


# 创建迭代器
def myGenerator():
    yield 0
    yield 1
    yield 2


for i in myGenerator():
    print i

print type(myGenerator())  # generator

# 或者
g = iter(myGenerator())
print g.next()
print g.next()
print g.next()
print '-' * 50


# 创建生成器函数,默认返回生成器
def generator(count=0):
    while count < 100:
        yield count
        count += 1
    # return count

