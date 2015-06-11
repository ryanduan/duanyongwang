# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'awang'

import sys
sys.path.insert(0, './models/')

import tornado.options
from tornado.options import options
import tornado.web
from tornado.httpserver import HTTPServer
import tornado.ioloop
from models.dao import Dao

from controller.dyw_controller import DYW
from controller.auth import AuthController


class Application(tornado.web.Application):
    """"""

    def __init__(self):
        """"""
        urls = [
            # (Controller.url, controller),
            (DYW.url, DYW),
            (AuthController.url, AuthController),
        ]
        settings = dict(
            xsrf_cookies=False,
            template_path='template',
            static_path='static',
            cookie_domain='.duanyong.wang',
            cookie_secret='de635135f4d0a75bc8368d5760d0b953',
        )
        tornado.web.Application.__init__(self, urls, **settings)

if __name__ == '__main__':
    """"""
    options.define(name='config', default='dev')
    options.define(name='port', default=9999)
    options.define(name='process', default=1)

    tornado.options.parse_command_line()

    Dao.init_db_uri(options.config)

    app = Application()
    server = HTTPServer(app, xheaders=True)
    server.bind(int(options.port))
    server.start(num_processes=int(options.process))

    tornado.ioloop.IOLoop.instance().start()