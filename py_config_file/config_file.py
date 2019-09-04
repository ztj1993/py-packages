# -*- coding: utf-8 -*-
# Intro: 配置文件模块
# Author: Ztj
# Email: ztj1993@gmail.com
# Version: 0.0.1
# Date: 2019-09-02

import json
import os.path
import time

import yaml

__version__ = '0.0.1'


class ConfigFile(object):
    """配置文件模块"""

    def __init__(self, config_dir):
        self.config_dir = config_dir
        self.yml_suffix = '.yml'
        self.json_suffix = '.json'

    def get_file_path(self, name, suffix, config_dir=None):
        """获取文件路径"""
        if config_dir is None:
            return os.path.join(self.config_dir, name) + suffix
        else:
            return os.path.join(config_dir, name) + suffix

    def get_exist(self, name, config_dir=None):
        """检查配置文件是否存在"""
        file_path = self.get_file_path(name, self.yml_suffix, config_dir)
        if os.path.isfile(file_path):
            return file_path
        file_path = self.get_file_path(name, self.json_suffix, config_dir)
        if os.path.isfile(file_path):
            return file_path
        return False

    def load(self, name, config_dir=None):
        """加载配置文件"""
        file_path = self.get_file_path(name, self.yml_suffix, config_dir)
        options = self.load_yml(file_path)
        if options is not None:
            return options
        file_path = self.get_file_path(name, self.json_suffix, config_dir)
        options = self.load_json(file_path)
        if options is not None:
            return options
        return None

    @staticmethod
    def load_json(file_path):
        """加载 JSON 配置文件"""
        if not os.path.isfile(file_path):
            return None
        with open(file_path) as f:
            return json.loads(f.read())

    @staticmethod
    def load_yml(file_path):
        """加载 YAML 配置文件"""
        if not os.path.isfile(file_path):
            return None
        with open(file_path) as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    @staticmethod
    def expire(file_path, callback, expires=3600):
        """文件失效"""
        is_expire = False
        if os.path.isfile(file_path) is False:
            is_expire = True
        else:
            st_m_time = os.stat(file_path).st_mtime
            if time.time() > (st_m_time + expires):
                is_expire = True
        if is_expire is True:
            file_content = callback()
            with open(file_path, 'w') as f:
                f.write(file_content)
        return is_expire
