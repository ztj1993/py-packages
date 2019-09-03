# -*- coding: utf-8 -*-
# Intro: MySQL 实例模块
# Author: Ztj
# Email: ztj1993@gmail.com
# Version: 0.0.1
# Date: 2019-07-08

import time

import pymysql
from DBUtils.PooledDB import PooledDB
from pymysql.connections import Connection
from pymysql.cursors import DictCursor
from registry import Registry

__version__ = '0.0.1'


class MySQL(object):

    def __init__(self, *args, **kwargs):
        self.options = Registry(kwargs.get('options', {}))
        self.pool = None
        self.server = None
        self.state = kwargs.get('state', True)

        self.options.default('host', '127.0.0.1')
        self.options.default('user', 'root')
        self.options.default('password', '')
        self.options.default('charset', 'utf8')

    def set_option(self, key, value):
        self.options.set(key, value)

    def get_pool(self) -> PooledDB:
        if self.pool is None:
            self.pool = PooledDB(creator=pymysql, cursorclass=DictCursor, **self.options.get())
        return self.pool

    def reconnect(self):
        self.pool = None
        self.server = self.get_pool().connection()

    def get_tmp_server(self) -> Connection:
        return self.get_pool().connection()

    def get_server(self) -> Connection:
        if self.server is None:
            self.server = self.get_pool().connection()
        return self.server

    def check_state(self) -> bool:
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
