# -*- coding: utf-8 -*-
# Intro: Redis 实例模块
# Author: Ztj
# Email: ztj1993@gmail.com
# Version: 0.0.1
# Date: 2019-09-03

import time

import redis
from registry import Registry

__version__ = '0.0.1'


class Redis(object):

    def __init__(self, *args, **kwargs):
        self.options = Registry(kwargs.get('options'))
        self.pool = None
        self.server = None
        self.state = kwargs.get('state', False)

        self.options.default('host', '127.0.0.1')
        self.options.default('port', 6379)
        self.options.default('db', 0)
        self.options.default('decode_responses', True)

    def set_option(self, key, value):
        self.options.set(key, value)

    def reconnect(self):
        self.pool = redis.ConnectionPool(**self.options.get())
        self.server = redis.Redis(connection_pool=self.pool)

    def get_server(self) -> redis.Redis:
        if self.server is None:
            self.reconnect()
        return self.server

    def check_state(self):
        try:
            self.server.ping()
            self.state = True
        except:
            self.state = False
        return self.state

    def check_wait(self, interval_time=60):
        while self.check_state() is False:
            time.sleep(interval_time)

    def __new__(cls, *args, **kwargs):
        instance = kwargs.get('instance', 0)
        if not hasattr(cls, '_instances'):
            cls._instances = {}
        if instance not in cls._instances:
            cls._instances[instance] = object.__new__(cls)
        return cls._instances[instance]
