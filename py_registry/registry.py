# -*- coding: utf-8 -*-
# Intro: 配置模块
# Author: Ztj
# Email: ztj1993@gmail.com
# Version: 0.0.1
# Date: 2019-09-02

import time

__version__ = '0.0.1'


class Registry(object):
    """ 配置模块"""

    def __init__(self, options=None):
        self.options = options if isinstance(options, dict) else {}
        self.hooks = {}
        self.separator = '.'

    def set(self, key, value):
        """设置配置项"""
        items = key if isinstance(key, list) else key.split(self.separator)
        # 弹出最后的键
        end_item = items.pop()
        # 执行默认值处理
        options = self.options
        for item in items:
            if not isinstance(options.get(item), dict):
                options[item] = {}
            options = options.get(item)
        # 设置新值
        options[end_item] = value
        return self.get(key)

    def unset(self, key, clear=False):
        """删除配置项"""
        items = key if isinstance(key, list) else key.split(self.separator)
        end_item = items.pop()
        options = self.get(items)
        if not isinstance(options, dict):
            return None
        item_value = options.pop(end_item)
        if clear is True and not options:
            self.unset(items, clear=True)
        return item_value

    def flat(self, key=None, skip=None, options=None):
        """扁平处理"""
        options = dict() if options is None else options
        skip = list() if skip is None else skip
        key_options = self.get(key)
        key_prefix = '' if key is None else key + self.separator
        for k, v in key_options.items():
            if key_prefix + k in skip:
                options[key_prefix + k] = v
            elif isinstance(v, dict):
                self.flat(key_prefix + k, skip, options)
            else:
                options[key_prefix + k] = v
        return options

    def merge(self, options, key=None):
        """合并配置"""
        if not isinstance(options, dict):
            return False
        # 递归合并
        key_prefix = '' if key is None else key + self.separator
        for k, v in options.items():
            if isinstance(v, dict):
                self.merge(v, key_prefix + k)
            else:
                self.set(key_prefix + k, v)
        return True

    def get(self, key=None, default=None, empty=False):
        """获取配置项"""
        if key is None or key == '':
            return self.options
        items = key if isinstance(key, list) else key.split(self.separator)
        # 处理数据
        options = self.options
        for item in items:
            options = options.get(item)
            if options is None:
                return default
        if empty:
            if not options:
                return default
        return options

    def append(self, key, value):
        """列表追加值"""
        target = self.get(key)
        if type(target) is not list:
            target = []
        target.append(value)
        self.set(key, target)

    def default(self, key=None, default=None):
        """设置默认值"""
        value = self.get(key)
        if value is None:
            self.set(key, default)
            return default
        return value

    def load(self, options):
        """加载配置项"""
        if isinstance(options, dict):
            self.options.update(options)
            return True
        else:
            return False

    def set_hook(self, key, overtime, callback):
        """设置钩子"""
        self.hooks[key] = dict()
        self.hooks[key]['last_time'] = int(time.time())
        self.hooks[key]['overtime'] = overtime
        self.hooks[key]['callback'] = callback

    def refresh_hook(self, key, *args, **kwargs):
        """刷新钩子"""
        hook = self.hooks[key]
        if hook is None:
            return None
        if (int(time.time()) - hook['last_time']) > hook['overtime']:
            hook['callback'](*args, **kwargs)
            hook['last_time'] = int(time.time())
            return True
        return False
