#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Leon Xu'
__email__ = 'cassvin91@gmail.com'
__date__ = '2013-09-15'


class Client(object):

    def __init__(self):
        raise NotImplementedError

    def login(self, username, password):
        raise NotImplementedError

    def logout(self):
        raise NotImplementedError

    @property
    def who(self):
        raise NotImplementedError
