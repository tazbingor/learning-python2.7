#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/27 下午7:09
# @Author  : Aries
# @Site    : 
# @File    : py023_tcp_server.py
# @Software: PyCharm
'''
创建一个TCP服务器

'''
from socket import *
from time import ctime

HOST = ""  # 表示bind()函数可以绑定在所有有效的地址上
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print "waiting for connection..."
    tcpCliSock, addr = tcpSerSock.accept()
    print "...connected from...", addr

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send("[%s]%s" % (ctime(), data))
    tcpCliSock.close()
tcpSerSock.close()
