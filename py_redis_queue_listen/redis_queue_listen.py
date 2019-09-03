# -*- coding: utf-8 -*-
# Intro: Redis 队列监听模块
# Author: Ztj
# Email: ztj1993@gmail.com
# Version: 0.0.1
# Date: 2019-09-04

import json
import logging
import time

import redis
from redis_instance import Redis

__version__ = '0.0.1'


class RedisQueueListen(object):
    """Redis 队列监听解析"""

    def __init__(self):
        self._redis_instance = None
        self.logger = logging.getLogger()
        self.queue_key = 'queue:listen:default'
        self.is_run = True
        self.redis_state = False
        self.queue_callback = None
        self.queue_sleep = 3
        self.queue_is_none = False
        self.queue_is_json = False

    @property
    def redis_instance(self) -> Redis:
        if self._redis_instance is None:
            self._redis_instance = Redis()
        return self._redis_instance

    @redis_instance.setter
    def redis_instance(self, instance: Redis):
        if isinstance(instance, Redis):
            self._redis_instance = instance
        else:
            self.logger.error('RedisInstanceError: run is end')
            self.is_run = False

    def listen(self):
        """监听执行"""
        self.redis_state = self.redis_instance.check_state()

        while self.is_run:
            # 检查 redis
            if self.redis_state is False and not self.redis_instance.check_state():
                self.logger.info('redis connect failure, waiting......')
                self.redis_instance.check_wait()
                self.redis_state = True
                self.logger.info('redis reconnect success, executing......')

            # 解析队列
            parse_result = self.parse()
            if parse_result is None:
                if self.queue_is_none is False:
                    self.logger.warning('queue is empty, running......')
                    self.queue_is_none = True
                else:
                    self.logger.debug('queue is empty, running......')
                time.sleep(self.queue_sleep)
                continue

    def parse(self):
        """解析数据"""
        try:
            data = self.redis_instance.get_server().rpop(self.queue_key)
            if data is None:
                return None
        except redis.exceptions.ConnectionError:
            self.redis_state = False
            return False

        # 设置队列是否为空
        if self.queue_is_none:
            self.queue_is_none = False

        # 解析 Json 数据
        if self.queue_is_json:
            try:
                data = json.loads(data)
            except json.decoder.JSONDecodeError:
                self.logger.error('JSONDecodeError: %s' % data)
                return False

        # 回调执行
        if self.queue_callback:
            self.logger.info('CallbackData: %s' % data)
            return self.queue_callback(data)
        else:
            self.logger.warning('NotCallbackData: %s' % data)
            return True
