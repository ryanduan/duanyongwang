# -*- coding: utf-8 -*-

"""
rcm: redis controller model
"""

from models.dao import Dao

__author__ = 'awang'


class RCM(object):
    """"""
    rds = Dao.redis()
    uid_psw = 'uid:psw'
    psw_uid = 'psw:uid'
    uid_name = 'uid:name'
    uid_nick = 'uid:nick'
    uid_incr = 'uid_incr'
    name_uid = 'name:uid'
    nick_uid = 'nick_uid'

    @classmethod
    def set(cls, key, value):
        cls.rds.set(key, value)

    @classmethod
    def mset(cls, data):
        """"""
        cls.rds.mset(**data)

    @classmethod
    def get(cls, key):
        return cls.rds.get(key)

    @classmethod
    def mget(cls, keys):
        return cls.rds.mget(keys)

    @classmethod
    def hget(cls, name, key):
        return cls.rds.hget(name, key)

    @classmethod
    def hset(cls, name, key, value):
        return cls.rds.hset(name, key, value)

    @classmethod
    def incr(cls, key):
        return cls.rds.incr(key)
