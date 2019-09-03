# -*- coding: utf-8 -*-
# Intro: Redis 队列监听模块安装文件
# Author: Ztj
# Email: ztj1993@gmail.com
# Date: 2019-09-04

import os.path
import re

from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf8')
readme = f.read()
f.close()

f = open(os.path.join(os.path.dirname(__file__), 'redis_queue_listen.py'), encoding='utf8')
version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)
f.close()

setup(
    name='py-ztj-redis-queue-listen',
    version=version,
    description='python redis queue listen package',
    long_description=readme,
    long_description_content_type="text/markdown",
    py_modules=["redis_instance"],
    url='http://github.com/ztj1993/PythonPackages/blob/master/py_redis_queue_listen',
    author='ZhangTianJie',
    author_email='ztj1993@gmail.com',
    keywords='redis, queue-parse, queue-listen',
    install_requires=['py-ztj-redis-instance'],
    license='MIT License',
)
