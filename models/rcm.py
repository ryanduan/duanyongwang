# -*- coding: utf-8 -*-

"""
rcm: redis controller model
"""

from models.dao import Dao

__author__ = 'awang'


class RCM(object):
    """"""
    rds = Dao.redis()

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