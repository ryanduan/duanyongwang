# -*- coding: utf-8 -*-

"""
Description
"""

__author__ = 'awang'

from controller.base_controller import BaseController
from models.terror import TError
from models.user import User


class AuthController(BaseController):
    """"""
    url = r'/dyw/login/?'

    def post(self, *args, **kwargs):
        """"""
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)
        if username is None or password is None:
            raise TError(code=2001, msg='username or password not valid')
        uid = User.login(username, password)
        if uid is None:
            if not User.username_exists(username):
                uid = User.register(username, password)
        if uid is None:  #
            self.redirect('/dyw/login')
            return
        self.session.set_session(dict(uid=uid))
        self.set_secure_cookie('sid', self.session.sid, domain=self.settings['cookie_domain'])
        self.redirect('/')

    def get(self, *args, **kwargs):
        """"""
        self.render('login.html')
