#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Leon Xu'
__email__ = 'cassvin91@gmail.com'
__date__ = '2013-09-15'


from common.client import Clinet as NeteaseClient


class WordBook(object):

    def __init__(self):
        self.client = NeteaseClient()

    def add_word(self, word):
        raise NotImplementedError

    def add_words(self, word):
        raise NotImplementedError

    def del_word(self, word):
        raise NotImplementedError

    def del_words(self, words):
        raise NotImplementedError

    def del_all(self):
        raise NotImplementedError

    def list_words(self):
        raise NotImplementedError
