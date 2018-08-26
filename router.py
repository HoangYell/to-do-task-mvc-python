# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, generators, division


# ===========================
#
#     [mvC] 3.1 Router
#
# ===========================


class Router:
    def __init__(self):
        self._routs = {}

    def register_controller(self, url, controller):
        self._routs[url] = controller

    def resolve(self, url):
        callback = self._routs.get(url)
        if callback:
            return callback
        return self.default_controller

    def default_controller(self, *args, **kwargs):
        status = '404 Not Found'
        body = b''
        return status, body
