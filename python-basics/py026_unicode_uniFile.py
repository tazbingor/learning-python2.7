#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/13 下午3:11
# @Author  : Aries
# @Site    : 
# @File    : py026_unicode_uniFile.py
# @Software: PyCharm
'''
python unicode
'''
CODEC = 'utf-8'
FILE = 'unicode.txt'

# 写入文本
hello_out = u'python'
bytes_out = hello_out.encode(CODEC)  # UTF8 格式化
f = open(FILE, 'w')
f.write(bytes_out)
f.close()

# 读取
f = open(FILE, 'r')
bytes_in = f.read()
f.close()
hello_in = bytes_in.encode(CODEC)
print hello_in,


'''
unicode 在实际应用中的原则
1. 程序中出现字符串时,一定要加前缀u
2. 不要使用str(), 用unicode代替
3. 不要使用过时的string模块
4. 不到必要时不要在程序中编码unicod的,只有在写入文件或者操作数据库时猜调用encode函数
    相应的,读取数据时才调用decode

'''