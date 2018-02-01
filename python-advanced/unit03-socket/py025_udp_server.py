#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/2/1 下午3:41
# @Author  : Aries
# @Site    : 
# @File    : py025_udp_server.py
# @Software: PyCharm
'''
创建一个UDP 服务器

伪代码
ss = socket() # 创建一个服务器套接字
ss.bind() # 绑定服务器套接字
inf_loop: # 服务器无限循环
cs = ss.recvfrom()/ss.sendto() # 对话（接收与发送）
ss.close() # 关闭服务器套接字
'''
from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print "waiting for message..."
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto("[%s]%s" % (ctime(), data), addr)
    print "...received from and returned to:", addr
udpSerSock.close()
