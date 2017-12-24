#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/24 上午10:23
# @Author  : Aries
# @Site    : 
# @File    : py116_user_register.py
# @Software: PyCharm
'''
13-4.
用户注册。
建立一个用户数据库（包括登录名、密码和上次登录时间戳）类（参考练习7-5和练习9-12），来管理一个系统。
该系统要求用户在登录后才能访问某些资源。
这个数据库类对用户进行管理，并在实例化操作时加载之前保存的用户信息，提供访问函数来添加或更新数据库的信息。
在数据修改后，数据库会在垃圾回收时将新信息保存到磁盘（参见__del__()）。
'''


# 简要的数据管理
class DBManagement(object):
    def __init__(self, username, password):
        self.name = username
        self.pwd = password

    def update_password(self, newpwd):
        self.pwd = newpwd
