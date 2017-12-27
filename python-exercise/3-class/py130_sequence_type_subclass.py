#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/27 下午7:45
# @Author  : Aries
# @Site    : 
# @File    : py130_sequence_type_subclass.py
# @Software: PyCharm
'''
13-18. 序列类型子类化。
模仿前面练习13-4中的用户注册类的解决方案，编写一个子类。
要求允许用户修改密码，但密码有效期是12个月，过期后不能重复使用。
'''
from datetime import datetime
import cPickle, os


class UserList(list):
    def __init__(self, dbfile, valid=4380):
        list.__init__([])
        self.valid = valid
        if os.path.exists(dbfile):
            f = file(dbfile)
            self.extend(cPickle.load(f))
            f.close()
        self.dbfile = dbfile
        self.flag = False

    def save(self):
        f = file(self.dbfile, 'w')
        cPickle.dump(self, f)
        f.close()

    def login(self, user, pwd):
        for i in range(len(self)):
            if self[i][0] == user and self[i][1] == pwd:
                dn = datetime.now().date()
                dr = self[i][2].date()
                if (dn - dr).days > self.valid:
                    print 'your pwd is expired,pls ask admin to change it'
                    self.flag = False
                    break
                else:
                    self.flag = True
                    break
            else:
                continue

    def deluser(self, num):
        if self.flag:
            self.pop(num)
        else:
            print 'login first'

    def updateuser(self, user, pwd):
        if self.flag:
            self.append([user, pwd, datetime.now()])
        else:
            print 'login first'

    def modifypwd(self, user, pwd):
        if self.flag:
            for i in range(len(self)):
                if self[i][0] == user:
                    self[i][1] = pwd
                    self[i][2] = datetime.now()

    def listall(self):
        if self.flag:
            print self
        else:
            print 'login first'


if __name__ == '__main__':
    user = UserList("cPickle.dat")
    user.login('root', 'root')
    user.listall()
    user.modifypwd('test2', 'test3')
    user.save()
    user.listall()
