#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/2/1 下午3:26
# @Author  : Aries
# @Site    : 
# @File    : py024_client.py
# @Software: PyCharm
'''
创建一个TCP客户端
'''
from socket import *

HOST = "192.168.37.21"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
    data = raw_input(">")
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data
tcpCliSock.close()
