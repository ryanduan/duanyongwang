# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'awang'


class TError(Exception):
    """"""

    def __init__(self, code=0, msg=''):
        self.code = code
        self.msg = msg
