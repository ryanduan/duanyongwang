# -*- coding: utf-8 -*-

"""
Description
"""
from controller.base_controller import BaseController
from models.rcm import RCM

__author__ = 'awang'


class DYW(BaseController):
    """"""
    url = r'/?'

    def get(self, *args, **kwargs):
        """"""
        title = 'T'
        data = dict(
            title=title,
            user=self.current_user,
        )
        self.render('dyw.html', **data)
