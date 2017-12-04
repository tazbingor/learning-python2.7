#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/16 下午11:20
# @Author  : Aries
# @Site    : 
# @File    : py041_IP_transducer.py
# @Software: PyCharm
'''
 IP transducer
 (a）创建一个从整型到IP地址的转换，如下格式：www.xxx.yyy.zzz。

（b）更新你的程序，使之可以逆转换。

'''

# 1 ip地址转换
ip = int(raw_input('please input a number as IP: \n'))
print 'IP' + '=' + str(int(int(ip) / 16777216) & 255) + '.' \
      + str(int(int(ip) / 65536) & 255) + '.' + str(int(int(ip) / 256) & 255) + '.' + str((int(ip) & 255))

print '-' * 50
# 2 ip你转换
ip = raw_input('please input a IP like xxx.xxx.xxx.xxx : \n')
print 'IP' + '=' + str(int(ip.split('.')[0]) * 16777216 + int(ip.split('.')[1]) * 65536 + \
                       int(ip.split('.')[2]) * 256 + int(ip.split('.')[3]))
