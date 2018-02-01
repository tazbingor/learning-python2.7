#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/2/1 下午3:45
# @Author  : Aries
# @Site    : 
# @File    : py026_udp_client.py
# @Software: PyCharm
'''
UDP客户端


'''
from socket import *

HOST = "192.168.37.21"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input(">")
    if not data:
        break
    udpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print data
udpCliSock.close()
