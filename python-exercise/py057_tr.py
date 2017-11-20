#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/20 下午6:31
# @Author  : Aries
# @Site    : 
# @File    : py057_tr.py
# @Software: PyCharm

'''
模拟Unix tr 替换删除字符

(a) 编写一个字符翻译程序(功能类似于Unix 中的tr 命令)。我们将这个函数叫做tr()，它有
三个字符串做参数: 源字符串、目的字符串、基本字符串，语法定义如下：
def tr(srcstr, dststr, string)
srcstr 的内容是你打算“翻译”的字符集合，dsrstr 是翻译后得到的字符集合，而string 是
你打算进行翻译操作的字符串。举例来说，如果srcstr == 'abc', dststr == 'mno', string =='abcdef', 那么tr()的输出将是'mnodef'.
注意这里len(srcstr) == len(dststr).
在这个练习里，你可以使用内建函数chr() 和 ord(), 但它们并不一定是解决这个问题所必不可少的函数。

(b) 在这个函数里增加一个标志符参数，来处理不区分大小写的翻译问题。

(c)修改你的程序，使它能够处理删除字符的操作。字符串srcstr 中不能够映射到字符串dststr中字符的多余字符都将被过滤掉。
换句话说，这些字符没有映射到dststr 字符串中的任何字符，因此就从函数返回的字符里被过滤掉了。
举例来说：如果 srcstr == 'abcdef', dststr == 'mno',string == 'abcdefghi', 那么tr()将输出'mnoghi'.
注意这里len(srcstr) >= len(dststr).

'''


# 如果srcstr == 'abc', dststr == 'mno', string =='abcdef', 那么tr()的输出将是'mnodef'.
def tr(srcstr, dststr, string):
    if (len(srcstr) >= len(dststr)) == False and \
                    srcstr not in string:
        return '输入有误'

    return subchr(string, srcstr, dststr)


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


print subchr('woodz', 'oo', 'pp')  # wppdz
print tr('Java', 'Python', 'JavaScript')  # PythonScript
