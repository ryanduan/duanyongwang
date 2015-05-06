# -*- coding: utf-8 -*-

"""
Description
"""
from tornado.web import RequestHandler

__author__ = 'awang'


class DYW(RequestHandler):
    """"""
    url = r'/?'

    def get(self, *args, **kwargs):
        """"""
        self.render('dyw.html')