#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/11/18 下午10:47
# @Author  : Aries
# @Site    : 
# @File    : py041_userpw.py
# @Software: PyCharm
'''
字典总结1
  这个程序用于管理用户的username和password, 当登录用户建立账户后,已存在用户可以用登录名字和密码返回系统
  新用户则不能用别人的登录名建立账号

'''

database = {}  # 模拟数据库


def newUser():
    prompt = 'login desired:\n'
    while True:
        name = raw_input(prompt)
        if database.has_key(name):
            prompt = 'name taken, try another: '
            continue
        else:
            break

    pwd = raw_input('password:\n')
    database[name] = pwd


def oldUser():
    name = raw_input('login:\n')
    pwd = raw_input('password:\n')
    password = database.get(name)
    if password == pwd and database.has_key(name):
        print 'welcome back', name
    else:
        print 'login incorrect'


def showMenu():
    propert = ''


newUser()
oldUser()
