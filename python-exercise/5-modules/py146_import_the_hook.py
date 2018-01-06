#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/6 下午8:54
# @Author  : Aries
# @Site    : 
# @File    : py146_import_the_hook.py
# @Software: PyCharm
'''
12–7. 导入钩子。
研究 PEP 302 的导入钩子机制.
实现你自己的导入机制, 允许编码你的模块(encryption, bzip2, rot13, 等), 这样解释器会自动解码它们并正确导入。
你可以参看 zip文件导入的实现 (参阅 第 12.5.7 节)。
'''
import sys
import imp
import base64

name = 'mytest'
f, path, desc = imp.find_module(name)

content = base64.decodestring(''.join(f))
with open('tmp', 'w') as fin:
    fin.write(content)
f = open('tmp')

module = imp.load_module(name, f, path, desc)
print sys.modules[name]
