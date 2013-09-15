#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Leon Xu'
__email__ = 'cassvin91@gmail.com'
__date__ = '2013-09-15'


import re
import time

import urllib
import urllib2
import cooklib

from common.decorator import login_required


class Client(object):
    login_url = 'https://reg.163.com/logins.jsp'
    logout_url = 'http://reg.163.com/logout.jsp'

    def __init__(self):
        self._user = None
        self._login = False

        cj = cooklib.CookieJar()
        self.opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(cj))

    def login(self, username, password, url='',
              savelogin=0, type=1, header_extra={}):
        # TODO: check if login

        payloads = (
            ('url', url),
            ('username', username),
            ('password', password),
            ('type', type),
            ('product', 163),
            ('savelogin', savelogin),
        )
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:17.0) \
                           Gecko/20100101 Firefox/17.0',
        }
        headers.update(header_extra)

        req = urllib2.Request(self.login_url,
                              urllib.urlencode(payloads))
        for key, value in headers.items():
            req.add_header(key, value)

        resp = self.opener.open(req)


    @login_required
    def logout(self):
        raise NotImplementedError

    def _extract(self, resp):
        raise NotImplementedError

    @property
    @login_required
    def who(self):
        return self._user
