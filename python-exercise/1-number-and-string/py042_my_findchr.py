#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/17 下午1:48
# @Author  : Aries
# @Site    : 
# @File    : py042_my_findchr.py
# @Software: PyCharm
'''
自定义findchr

（a）创建一个名字为findchr()的函数，函数声明如下。

def findchr(string, char)

findchr()要在字符串string中查找字符char，找到就返回该值得索引，否则返回-1。不能用string.find()或者string.index()函数和方法。

（b）创建另一个叫rfindchr()的函数，查找字符char最后一次出现的位置。它跟findchr()工作类似，不过它是从字符串的最后开始向前查找的。

（c）创建第三个函数，名字叫subchr()，声明如下。

def subchr(string, origchar, newchar)

subchr()跟findchr()类似，不同的是，如果找到匹配的字符就用新的字符替换原先字符。返回修改后的字符串。

'''


# findchr
def findchr(str, char):
    result = 0
    strlen = len(str)
    if char in str:
        for i in range(strlen):
            if char == str[i]:
                result = i
                break
    else:
        result = -1

    return result


# print findchr('woodz', 'o')
# print findchr('滚滚长江东逝水', '长江')
print findchr('findchr', 'c')  # 4
print findchr('findchr', 'z')  # -1

print '-' * 50


# rfindchr
def rfindchr(str, char):
    result = 0
    strlen = len(str)
    if char in str:
        for i in range(strlen):
            if char == str[-1 - i]:
                result = strlen - i - 1
                break
    else:
        result = -1

    return result


print rfindchr('javascript', 'c')
print rfindchr('versions', 'si')
print '-' * 50


# def subchr(string, origchar, newchar)
def subchr(string, origchar, newchar):
    length_o = len(origchar)
    length_s = len(string)
    newstring = ""
    i = 0
    while i < length_s:
        if string[i:i + length_o] == origchar:
            newstring += newchar
            i += length_o
        else:
            newstring += string[i]
            i += 1
    return newstring


print subchr('woodz', 'oo', 'pp')
print subchr('woodz', 'oo', '[woodz]')
