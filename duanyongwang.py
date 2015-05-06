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


class Application(tornado.web.Application):
    """"""

    def __init__(self):
        """"""
        urls = [
            # (Controller.url, controller),
            (DYW.url, DYW),
        ]
        settings = dict(
            xsrf_cookies=False,
            template_path='template',
        )
        tornado.web.Application.__init__(self, urls, **settings)

if __name__ == '__main__':
    """"""
    options.define(name='config', default='dev')
    options.define(name='port', default=21002)
    options.define(name='process', default=1)

    tornado.options.parse_command_line()

    # Dao.init_db_uri(options.config)

    app = Application()
    server = HTTPServer(app, xheaders=True)
    server.bind(port=21001, )
    server.start(num_processes=int(options.process))

    tornado.ioloop.IOLoop.instance().start()