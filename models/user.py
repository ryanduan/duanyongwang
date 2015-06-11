# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'awang'

import hashlib
from models.rcm import RCM
from models.terror import TError
import re


deny_list = ['root', 'admin', ]


class User(object):
    """"""
    uid_psw = 'uid:psw'
    psw_uid = 'psw:uid'
    uid_name = 'uid:name'
    uid_nick = 'uid:nick'
    uid_incr = 'uid_incr'
    name_uid = 'name:uid'
    nick_uid = 'nick_uid'

    def __init__(self, uid=None):
        self.uid = uid

    @property
    def username(self):
        """"""
        return RCM.hget(self.uid_name, self.uid)

    @classmethod
    def login(cls, username, password):
        """"""
        psw = cls.encrypt(username, password)
        uid = RCM.hget(RCM.psw_uid, psw)
        return uid or None

    @classmethod
    def encrypt(cls, username, password):
        """"""
        salt = hashlib.md5()
        salt.update('{}{}'.format(username[::-1], password[-2:-5:-1]))
        psw = salt.hexdigest()[-2:-8:-1]
        sp = hashlib.sha1()
        sp.update(password + psw)
        return sp.hexdigest()

    @classmethod
    def register(cls, username, password):
        """"""
        cls.check_username(username)
        if password < 6:
            raise TError(code=1002, msg='password too short')
        uid = cls.get_uid_by_name(username)
        psw = cls.encrypt(username, password)
        RCM.hset(RCM.uid_psw, uid, psw)
        RCM.hset(RCM.psw_uid, psw, uid)
        return uid

    @classmethod
    def get_uid_by_name(cls, username):
        """"""
        uid = RCM.hget(RCM.uid_name, username)
        if uid:
            return uid
        uid = RCM.incr(RCM.uid_incr)
        RCM.hset(RCM.uid_name, uid, username)
        RCM.hset(RCM.name_uid, username, uid)
        return uid

    @classmethod
    def check_username(cls, username):
        """"""
        if username == 'T' or username == 't':
            return True
        ru = r'^[a-z][a-z0-9_\-\.@]+$'
        if 3 < len(username) < 16:
            raise TError(code=1001, msg='username length out of range')
        if not re.match(ru, username) or username in deny_list:
            raise TError(code=1004, msg='username not valid')
        if cls.username_exists(username):
            raise TError(code=1003, msg='username is exists')
        return True

    @classmethod
    def username_exists(cls, username):
        """"""
        uid = RCM.hget(RCM.uid_name, username)
        if uid:
            return True
        return False
