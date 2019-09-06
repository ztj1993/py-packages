# -*- coding: utf-8 -*-
# Intro: Aria2 本地管理模块
# Author: Ztj
# Email: ztj1993@gmail.com
# Version: 0.0.1
# Date: 2019-09-06

import subprocess

import psutil
from registry import Registry

__version__ = '0.0.1'


class Aria2Local(object):
    process: subprocess.Popen or None

    def __init__(self, program='aria2c', **kwargs):
        self.program = program
        self.process = None
        self.args = Registry(kwargs.get('args'))
        self.args.default('rpc-listen-port', '6800')
        self.args.default('enable-rpc', 'true')
        self.args.default('rpc-allow-origin-all', 'true')
        self.args.default('rpc-listen-all', 'true')

    def set_arg(self, key, value):
        self.args.set(key, value)

    def get_args_string(self):
        return ' '.join(['--%s=%s' % (key, value) for key, value in self.args.get().items()])

    def start(self):
        """启动服务"""
        cmd = '%s %s' % (self.program, self.get_args_string())
        self.process = subprocess.Popen(cmd, shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return self.process.pid

    def stop(self):
        """停止服务"""
        if self.process is not None:
            parent = psutil.Process(self.process.pid)
            for child in parent.children(recursive=True):
                child.terminate()
            parent.terminate()
            return self.process.wait()
        else:
            return None

    def is_install(self):
        """是否安装"""
        cmd = '%s --version' % self.program
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stderr_line = process.stderr.readline()
        if stderr_line == b'':
            return True
        else:
            return False

    def is_running(self):
        """是否运行"""
        return self.process is not None and self.process.poll() is None
