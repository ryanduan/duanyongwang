# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'awang'

from tornado.web import RequestHandler
from models import Dao
from models import Session
from models import User


class BaseController(RequestHandler):
    """"""

    @property
    def rds(self):
        return Dao.redis()

    @property
    def current_user(self):
        """"""
        return User(self.current_uid)

    @property
    def current_uid(self):
        """"""
        return self.session.data.get('uid', None)

    @property
    def session(self):
        """"""
        new_session = Session(self.current_sid)
        if not self.current_sid:
            # print('Set sid to cookie: {}'.format(new_session.sid))
            self.set_secure_cookie('sid', new_session.sid, domain=self.settings['cookie_domain'])
            print(self.settings['cookie_domain'])
            # sid = self.create_signed_value('sid', new_session.sid)
            # self.set_cookie('sid', sid, domain=None)
            # print(self.create_signed_value('sid', new_session.sid))
        return new_session

    @property
    def current_sid(self):
        """"""
        # if not self.get_secure_cookie('sid'):
        #     return Session().sid
        # print('Start get sid from cookie: {}'.format(self.get_secure_cookie('sid')))
        return self.get_secure_cookie('sid')

