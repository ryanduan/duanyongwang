# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'awang'

from models import Dao
from uuid import uuid4
import json


class Session(object):
    """"""

    def __init__(self, sid=None):
        """"""
        self.expire = 30 * 26 * 60 * 60
        self.sid = sid or uuid4().hex
        self.rds = Dao.redis()
        self.data = self.__data
        self.set_session(self.data)

    def set_session(self, data):
        """"""
        self.rds.set(self.sid, json.dumps(data))
        self.rds.expire(self.sid, self.expire)

    @property
    def __data(self):
        """"""
        res = self.rds.get(self.sid)
        if res:
            return json.loads(res)
        return {}
