#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/1/2 下午8:13
# @Author  : Aries
# @Site    : 
# @File    : py118_create_error.py
# @Software: PyCharm
'''
创建异常
'''
import os, socket, errno, types, tempfile


class NetworkError(IOError): pass


class FileError(IOError): pass


def updArgs(args, newarg=None):
    if isinstance(args, IOError):
        myargs = []
        myargs.extend([arg for arg in args])
    else:
        myargs = list(args)

    if newarg:
        myargs.append(newarg)

    return tuple(myargs)


def fileArgs(file, mode, args):
    if args[0] == errno.Eacces and 'access' in dir(os):
        perms = ''
        permd = {
            'r': os.R_OK,
            'w': os.W_OK,
            'x': os.X_OK
        }
        pkeys = permd.keys()
        pkeys.sort()
        pkeys.reverse()

        for eachPerm in 'rwx':
            if os.access(file, permd[eachPerm]):
                perms += eachPerm
            else:
                perms += '-'

        if isinstance(args, IOError):
            myargs = []
            myargs.extend([arg for arg in args])
        else:
            myargs = list(args)

        myargs[1] = "'%s' %s(perms: '%s')" % (mode, myargs[1], perms)
        myargs.append(args.filename)

    else:
        myargs = args

    return tuple(myargs)


def myconnect(sock, host, port):
    try:
        sock.connect((host, port))
    except socket.error, args:
        myargs = updArgs(args)
        if len(myargs) == 1:
            myargs = (errno.ENXIO, myargs[0])

        raise NetworkError, updArgs(myargs, host + ': ' + str(port))
