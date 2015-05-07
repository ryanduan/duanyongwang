# -*- coding: utf-8 -*-

"""
Description
"""
from tornado.web import RequestHandler
from models.rcm import RCM

__author__ = 'awang'


class DYW(RequestHandler):
    """"""
    url = r'/?'

    def get(self, *args, **kwargs):
        """"""
        title = RCM.get('hp_tl')
        data = dict(
            title=title,
        )
        self.render('dyw.html', **data)