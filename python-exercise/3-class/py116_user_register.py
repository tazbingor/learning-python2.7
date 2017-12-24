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


# 数据管理类
class DBManagement(object):
    def __init__(self, username='admin', password='admin'):
        self.user_db = {}
        self.user_db[username] = password

    def update_password(self, username, newpwd):
        self.user_db[username] = newpwd


# 用户登录类
class UserLoginAndRegister(object):
    def __init__(self):
        self.db_manage = DBManagement()

    def register(self):
        prompt = 'login desired:\n'
        while True:
            name = raw_input(prompt)
            if self.db_manage.user_db.has_key(name):
                prompt = 'name taken, try another: '
                continue
            else:
                break

        pwd = raw_input('password:\n')
        self.db_manage.user_db[name] = pwd

    def login(self):
        name = raw_input('login:\n')
        pwd = raw_input('password:\n')
        password = self.db_manage.user_db.get(name)
        if password == pwd and \
                self.db_manage.user_db.has_key(name):
            print 'welcome back', name
        else:
            print 'login incorrect'

    def show_users(self):
        for each_item in self.db_manage.user_db:
            print 'username:', each_item, \
                ',pwd:', self.db_manage.user_db[each_item]

    def change_password(self):
        username = raw_input('Please enter the username')
        newpwd = raw_input('Please enter a new password')
        self.db_manage.user_db[username] = newpwd


if __name__ == '__main__':
    user = UserLoginAndRegister()
    user.register()
    user.login()
    user.show_users()
    user.change_password()
    user.login()
    user.show_users()
